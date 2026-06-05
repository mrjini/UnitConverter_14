# 05 — Validation Spec (검증 규칙 명세)

## 1. 검증 순서

입력은 아래 순서로 검증한다. **첫 실패 시 즉시 중단.**

```
1. Format (콜론·비어 있지 않음)     ← boundary.InputParser
2. Number  (float 파싱)            ← boundary.InputParser
3. Negative (value >= 0)           ← entity.Validator
4. Unit    (Registry 존재)         ← entity.Validator
```

**ECB:** 1~2는 boundary, 3~4는 entity. control.ConvertUseCase가 순서를 조율.

---

## 2. 규칙 상세

### VAL-R01 — 형식 (ERR_FORMAT)

| 조건 | 결과 |
|------|------|
| `:` 없음 | ERR_FORMAT |
| `unit` 빈 문자열 (`:2.5`) | ERR_FORMAT |
| `value` 빈 문자열 (`meter:`) | ERR_FORMAT |
| 공백만 (` `, `meter: `) | ERR_FORMAT 또는 ERR_NUMBER |

**메시지:** `Invalid format. Use unit:value (ex: meter:2.5)`

**Test ID:** VAL-02

---

### VAL-R02 — 숫자 (ERR_NUMBER)

| 조건 | 결과 |
|------|------|
| `value`가 `float()` 불가 (`abc`, `1.2.3`) | ERR_NUMBER |

**메시지:** `Invalid number: {value_str}`

**Test ID:** VAL-02b (시나리오 카탈로그)

---

### VAL-R03 — 음수 (ERR_NEGATIVE)

| 조건 | 결과 |
|------|------|
| `value < 0` | ERR_NEGATIVE |
| `value == 0` | **허용** |

**메시지:** `Negative value not allowed: {value}`

**Test ID:** VAL-01

---

### VAL-R04 — 미등록 단위 (ERR_UNKNOWN_UNIT)

| 조건 | 결과 |
|------|------|
| `unit` not in Registry | ERR_UNKNOWN_UNIT |

**메시지:** `Unknown unit: {unit}`

**Test ID:** VAL-03

---

### VAL-R05 — 설정 파일 (ERR_CONFIG) [P2]

| 조건 | 결과 |
|------|------|
| 파일 없음 | ERR_CONFIG |
| JSON/YAML 파싱 실패 | ERR_CONFIG |
| 필수 필드 누락 | ERR_CONFIG |
| 비율 ≤ 0 | ERR_CONFIG |

**메시지:** `Config error: {detail}`

**Test ID:** CFG-02

---

### VAL-R06 — 동적 등록 (ERR_REGISTRATION) [P2]

| 조건 | 결과 |
|------|------|
| 패턴 불일치 | ERR_REGISTRATION |
| ratio ≤ 0 | ERR_REGISTRATION |
| 중복 unit명 (정책: 덮어쓰기 또는 거부 — **거부**) | ERR_REGISTRATION |

**패턴:** `^1\s+(\w+)\s+=\s+([\d.]+)\s+meter$`

**Test ID:** REG-02

---

## 3. Test ID ↔ 규칙 매핑

| Test ID | 규칙 | ECB | 입력 예 | 기대 |
|---------|------|-----|---------|------|
| VAL-01 | VAL-R03 | entity | `meter:-1` | exit 1, ERR_NEGATIVE |
| VAL-02 | VAL-R01 | boundary | `meter2.5` | exit 1, ERR_FORMAT |
| VAL-02b | VAL-R02 | boundary | `meter:abc` | exit 1, ERR_NUMBER |
| VAL-03 | VAL-R04 | entity | `mile:1` | exit 1, ERR_UNKNOWN_UNIT |
| VAL-04 | VAL-R01 | boundary | `meter:` | exit 1, ERR_FORMAT |
| VAL-05 | VAL-R03 | entity | `feet:0` | exit 0, 정상 변환 |

---

## 4. Mom Test 연결

| Mom Test 증거 | 검증 규칙 |
|---------------|-----------|
| 형식 검증 누락 → 팀원 질문 후 추가 | VAL-R01, VAL-R02 — P0 필수 |
| 상수 불일치 40분 | VAL-* + CONV-* 회귀로 재발 방지 |
| 수동 비교표 1시간 | Test ID로 자동 회귀 (SC-3) |

---

## 5. RED 단계 작성 지침

- pytest `parametrize`로 Test ID를 테스트 함수 docstring 또는 `@pytest.mark` id에 명시
- 오류 케이스: stdout 비어 있음, stderr 메시지 partial match, exit code assert
- **SPEC 단계에서는 pytest 코드 작성하지 않음**
