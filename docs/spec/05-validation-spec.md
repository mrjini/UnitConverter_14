# 05 — Validation Spec (검증 규칙 명세)

## 1. 검증 순서

입력은 아래 순서로 검증한다. **첫 실패 시 즉시 중단.**

```
1. Format (콜론·비어 있지 않음)     ← boundary.InputParser  → ParseError
2. Number  (float 파싱)            ← boundary.InputParser  → ParseError
3. Negative (value >= 0)           ← entity.Validator      → ValidationError
4. Unit    (Registry 존재)         ← entity.Validator      → ValidationError
```

**ECB:** 1~2는 **boundary**(CLI+InputParser). 3~4는 **entity**(ConvertUseCase→Validator).  
**control은 boundary를 import하지 않음** — CLI가 파싱 후 `(unit, value)` 전달.

## 1.1 이중 테스트 전략

| 단계 | Logic Track assert | UI Track assert |
|------|-------------------|-----------------|
| 1~2 | `ParseError.code` | CLI exit 1 + stderr (CLI-04) |
| 3~4 | `ValidationError.code` | CLI exit 1 + stderr (CLI-03) |

---

## 2. 규칙 상세

### VAL-R01 — 형식 (ERR_FORMAT)

| 조건 | 결과 |
|------|------|
| `:` 없음 | ERR_FORMAT |
| `unit` 빈 문자열 (`:2.5`) | ERR_FORMAT |
| `value` 빈 문자열 (`meter:`) | ERR_FORMAT |
| 공백만 (` `, `meter: `) | ERR_FORMAT 또는 ERR_NUMBER |

**예외:** `boundary.input_parser.ParseError`  
**메시지:** `Invalid format. Use unit:value (ex: meter:2.5)`  
**Test ID:** VAL-02, VAL-04 | **Harness:** `tests/boundary/test_input_parser.py`

---

### VAL-R02 — 숫자 (ERR_NUMBER)

| 조건 | 결과 |
|------|------|
| `value`가 `float()` 불가 | ERR_NUMBER |

**예외:** `ParseError`  
**메시지:** `Invalid number: {value_str}`  
**Test ID:** VAL-02b

---

### VAL-R03 — 음수 (ERR_NEGATIVE)

| 조건 | 결과 |
|------|------|
| `value < 0` | ERR_NEGATIVE |
| `value == 0` | **허용** |

**예외:** `entity.validator.ValidationError`  
**메시지:** `Negative value not allowed: {value}`  
**Test ID:** VAL-01 | **Harness:** `tests/entity/`

---

### VAL-R04 — 미등록 단위 (ERR_UNKNOWN_UNIT)

| 조건 | 결과 |
|------|------|
| `unit` not in Registry | ERR_UNKNOWN_UNIT |

**예외:** `ValidationError`  
**Test ID:** VAL-03

---

### VAL-R05 — 설정 파일 (ERR_CONFIG) [P2]

**Test ID:** CFG-02

### VAL-R06 — 동적 등록 (ERR_REGISTRATION) [P2]

**Test ID:** REG-02

---

## 3. Test ID ↔ 규칙 매핑

| Test ID | 규칙 | ECB | Harness | Logic assert | UI |
|---------|------|-----|---------|--------------|-----|
| VAL-01 | VAL-R03 | entity | tests/entity | ValidationError | CLI-03 |
| VAL-02 | VAL-R01 | boundary | test_input_parser | ParseError | CLI-04 |
| VAL-02b | VAL-R02 | boundary | test_input_parser | ParseError | CLI-04 |
| VAL-03 | VAL-R04 | entity | tests/entity | ValidationError | — |
| VAL-04 | VAL-R01 | boundary | test_input_parser | ParseError | CLI-04 |
| VAL-05 | VAL-R03 | entity | tests/entity | 정상 변환 | CLI-02 |

---

## 4. Mom Test 연결

| Mom Test 증거 | 검증 규칙 |
|---------------|-----------|
| 형식 검증 누락 | VAL-R01/R02 — P0, Logic+UI 이중 |
| 상수 불일치 40분 | VAL-* + CONV-* 회귀 |

---

## 5. RED 단계 작성 지침

- Logic: `ValidationError` / `ParseError` assert — **exit code assert 금지**
- UI: subprocess/CLI — exit code + stderr
- **SPEC 단계에서는 pytest 코드 작성하지 않음**
