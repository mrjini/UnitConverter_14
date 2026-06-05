# 10 — Dual-Track TDD Plan (ECB)

## 1. 개요

Dual-Track TDD는 **Logic Track(entity/control/InputParser 단위)** 과 **UI Track(CLI E2E)** 을 분리한다.

| 문서 | Cursor / Harness |
|------|------------------|
| **Track A** | **Logic** — Domain Mock 금지 |
| **Track B** | **UI** — stdin/stdout Mock 허용 |

---

## 2. Track 정의

| Track | 범위 | Test 접두 | ECB | Harness |
|-------|------|-----------|-----|---------|
| **Logic** | 변환, meter 경유, Validator | CONV-*, VAL-01,03,05 | entity | `tests/entity/` |
| **Logic** | InputParser 단위 | VAL-02, 02b, 04 | boundary | `tests/boundary/test_input_parser.py` |
| **Logic** | UseCase | ConvertUseCase | control | `tests/control/` |
| **UI** | CLI, 포맷, 설정 E2E | FMT-*, CLI-*, CFG-*, REG-* | boundary, infrastructure | `tests/boundary/` |

---

## 3. RED 사이클 순서

### Cycle 1 — entity (red → green, P0)

```
RED:   CONV-01 → CONV-04 → VAL-01 → VAL-03 → VAL-05
       tests/entity/
GREEN: entity/converter, validator, registry
```

### Cycle 1b — boundary InputParser (red → green, P0)

```
RED:   VAL-02 → VAL-02b → VAL-04
       tests/boundary/test_input_parser.py
GREEN: boundary/input_parser.py (ParseError)
```

### Cycle 1c — control (red → green, P0)

```
RED:   ConvertUseCase + entity 통합
       tests/control/
GREEN: control/convert_use_case.py
```

### Cycle 2 — UI boundary (red → green, P0)

```
RED:   FMT-01 → CLI-02 → CLI-03 → CLI-04
       tests/boundary/
GREEN: boundary/cli, formatter/table
REFACTOR: Formatter Protocol
```

### Cycle 3~5 — P2 (new_features)

(변경 없음: CFG, REG, FMT-02/03)

---

## 4. 검증 이중 전략

| Test ID | Logic (단위) | UI (E2E) |
|---------|--------------|----------|
| VAL-01 | `ValidationError` ERR_NEGATIVE | CLI-03 exit 1 |
| VAL-02~04 | `ParseError` | CLI-04 exit 1 |
| VAL-03 | `ValidationError` ERR_UNKNOWN_UNIT | (CLI 확장 optional) |

---

## 5. 테스트 디렉터리 (RED에서 생성)

```
tests/
├── entity/
│   test_converter.py      # CONV-*
│   test_validator.py      # VAL-01, VAL-03, VAL-05
├── control/
│   test_convert_use_case.py
├── boundary/
│   test_input_parser.py   # VAL-02, VAL-02b, VAL-04
│   test_cli.py            # CLI-*
│   test_formatters.py     # FMT-*
│   test_config.py         # CFG-*
│   test_registration.py   # REG-*
└── conftest.py
```

---

## 6~8. (ARRR, Mom Test, RED checklist)

- 08-design-spec ECB 의존: **CLI → InputParser → ConvertUseCase(unit,value) → entity**
- Mom Test 형식 검증: VAL-02/04 (Logic) + CLI-04 (UI)

## RED 착수 체크리스트

- [ ] 09-scenario-catalog P0 확정 (CLI-03, CLI-04 포함)
- [ ] 11-matrix TODO-013 / TODO-019 분리
- [ ] spec → red
