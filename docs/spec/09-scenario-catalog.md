# 09 — Scenario Catalog (시나리오 카탈로그)

> Given-When-Then 형식. **pytest 코드 없음** — RED 단계에서 구현.

## Track 명칭

| 문서 Track | Cursor Track | 설명 |
|------------|--------------|------|
| **Track A** | **Logic** | entity/control + boundary 단위(InputParser). Domain Mock 금지 |
| **Track B** | **UI** | CLI E2E, 포맷, 설정. stdin/stdout Mock 허용 |

## ECB ↔ Track ↔ Harness

| Track | ECB | Test Harness | Test 접두 |
|-------|-----|--------------|-----------|
| A (Logic) | entity | `tests/entity/` | CONV-*, VAL-01, VAL-03, VAL-05 |
| A (Logic) | control | `tests/control/` | ConvertUseCase |
| A (Logic) | boundary (단위) | `tests/boundary/test_input_parser.py` | VAL-02, VAL-02b, VAL-04 |
| B (UI) | boundary (E2E) | `tests/boundary/test_cli.py` 등 | FMT-*, CLI-* |
| B (UI) | infrastructure (E2E) | `tests/boundary/` | CFG-*, REG-* |

## 검증 이중 전략

| 계층 | Test ID | Logic assert | UI assert (CLI/E2E) |
|------|---------|--------------|---------------------|
| entity | VAL-01, 03, 05 | `ValidationError` + code | CLI-02 등에서 exit + stderr |
| boundary | VAL-02, 02b, 04 | `ParseError` + code | CLI-02 등에서 exit + stderr |

---

## Track A — Logic (entity / control / InputParser)

### CONV — 변환

#### CONV-01: meter 입력 기본 변환

| | |
|---|---|
| **Given** | Registry에 meter, feet, yard 등록 |
| **When** | unit=`meter`, value=`2.5` 변환 |
| **Then** | meter=2.5, feet=8.2, yard=2.7 (display 1자리) |
| **PRD** | PRD-001, 003, 008, 009 |
| **ECB** | entity (`entity.converter`) |
| **Harness** | `tests/entity/` |

#### CONV-02: feet 입력 변환

| | |
|---|---|
| **Given** | Registry 기본 3단위 |
| **When** | unit=`feet`, value=`8.2` |
| **Then** | meter=2.5, feet=8.2, yard 출력 (meter 경유, display 1자리) |
| **PRD** | PRD-001, 004 |

#### CONV-03: yard 입력 변환

| | |
|---|---|
| **Given** | Registry 기본 3단위 |
| **When** | unit=`yard`, value=`2.7` |
| **Then** | meter=2.5, feet/yard 포함 전 단위 출력 (display 1자리) |
| **PRD** | PRD-001, 004 |

#### CONV-04: meter 경유 일관성 (feet→yard)

| | |
|---|---|
| **Given** | Registry 기본 3단위 |
| **When** | unit=`feet`, value=`3.28084` |
| **Then** | yard display = **1.0** |
| **PRD** | PRD-004 |
| **Note** | 직접 feet→yard 상수 사용 시 **실패** |

#### CONV-05: cubit 포함 변환 [P2]

| | |
|---|---|
| **Given** | cubit 등록 (`to_meter_factor=0.4572`) |
| **When** | unit=`cubit`, value=`1` |
| **Then** | meter display=**0.5** (raw 0.4572 → 1자리), feet/yard/cubit 출력 |
| **PRD** | PRD-014 |
| **Golden** | `docs/spec/06-conversion-rules.md` §4 cubit 행 |

---

### VAL — entity (Logic)

#### VAL-01: 음수 거부

| | |
|---|---|
| **Given** | Registry 기본 |
| **When** | Validator에 unit=`meter`, value=`-1` |
| **Then** | `ValidationError`, code=`ERR_NEGATIVE` |
| **PRD** | PRD-005 |
| **Harness** | `tests/entity/` |

#### VAL-03: 미등록 단위

| | |
|---|---|
| **Given** | Registry 기본 |
| **When** | unit=`mile`, value=`1` |
| **Then** | `ValidationError`, code=`ERR_UNKNOWN_UNIT` |
| **PRD** | PRD-007 |

#### VAL-05: 영 허용

| | |
|---|---|
| **Given** | Registry 기본 |
| **When** | unit=`feet`, value=`0` |
| **Then** | 정상 변환, 모든 단위 display=0 |
| **PRD** | PRD-005 |

---

### VAL — boundary InputParser (Logic, 단위 테스트)

#### VAL-02: 형식 오류 — 콜론 없음

| | |
|---|---|
| **When** | `InputParser.parse("meter2.5")` |
| **Then** | `ParseError`, code=`ERR_FORMAT` |
| **PRD** | PRD-006 |
| **Harness** | `tests/boundary/test_input_parser.py` |

#### VAL-02b: 숫자 오류

| | |
|---|---|
| **When** | `InputParser.parse("meter:abc")` |
| **Then** | `ParseError`, code=`ERR_NUMBER` |
| **PRD** | PRD-006 |

#### VAL-04: 빈 값

| | |
|---|---|
| **When** | `InputParser.parse("meter:")` |
| **Then** | `ParseError`, code=`ERR_FORMAT` |
| **PRD** | PRD-006 |

---

## Track B — UI (boundary E2E / infrastructure)

### FMT — 출력 포맷

#### FMT-01: table 기본 [P0]

| | |
|---|---|
| **Given** | format=table (default) |
| **When** | stdin `meter:2.5` |
| **Then** | 3줄, `{v} {unit} = {tv} {tunit}` 형식 |
| **PRD** | PRD-008 |

#### FMT-02: json [P2]

| | |
|---|---|
| **Given** | `--format json` |
| **When** | `meter:2.5` |
| **Then** | valid JSON array, io-contract 준수 |
| **PRD** | PRD-015 |

#### FMT-03: csv [P2]

| | |
|---|---|
| **Given** | `--format csv` |
| **When** | `meter:2.5` |
| **Then** | header + 3 data rows |
| **PRD** | PRD-016 |

---

### CFG — 설정

#### CFG-01: JSON 로드 [P2]

| | |
|---|---|
| **Given** | valid units.json |
| **When** | `--config units.json`, `meter:2.5` |
| **Then** | CONV-01과 동일 결과 |
| **PRD** | PRD-013 |

#### CFG-02: 잘못된 설정 [P2]

| | |
|---|---|
| **Given** | broken.json |
| **When** | `--config broken.json` |
| **Then** | ERR_CONFIG, exit 2 |
| **PRD** | PRD-013 |

---

### REG — 동적 등록

#### REG-01: cubit 등록 [P2]

| | |
|---|---|
| **Given** | — |
| **When** | `--register "1 cubit = 0.4572 meter"`, `cubit:1` |
| **Then** | cubit in output, CONV-05 |
| **PRD** | PRD-014 |

#### REG-02: 잘못된 registration [P2]

| | |
|---|---|
| **When** | `--register "bad"` |
| **Then** | ERR_REGISTRATION, exit 2 |
| **PRD** | PRD-014 |

---

### CLI — 통합 (UI, exit code 검증)

#### CLI-01: help [P1]

| | |
|---|---|
| **When** | `--help` |
| **Then** | usage 출력, exit 0 |

#### CLI-02: E2E meter [P0]

| | |
|---|---|
| **When** | stdin `meter:2.5`, default options |
| **Then** | FMT-01 + exit 0 |

#### CLI-03: E2E 검증 오류 [P0]

| | |
|---|---|
| **When** | stdin `meter:-1` |
| **Then** | ERR_NEGATIVE stderr, exit 1 |
| **PRD** | PRD-005 (UI 측 VAL-01) |

#### CLI-04: E2E 형식 오류 [P0]

| | |
|---|---|
| **When** | stdin `meter2.5` |
| **Then** | ERR_FORMAT stderr, exit 1 |
| **PRD** | PRD-006 (UI 측 VAL-02) |

---

## P1 — 설계 검증 (수동 / review-ecb)

| Test ID | PRD | 방법 |
|---------|-----|------|
| **ARCH-01** | PRD-010 | `/review-ecb` OCP 체크 + CONV/FMT 회귀 green |
| **ARCH-02** | PRD-011 | `/review-ecb` ECB/SRP 체크리스트 Pass |
| **(meta)** | PRD-012 | `11-traceability-matrix.md` orphan 0건 |

---

## 우선순위 요약

| Priority | Test IDs |
|:--------:|----------|
| **P0** | CONV-01~04, VAL-01~05, FMT-01, CLI-02~04 |
| **P1** | CLI-01, ARCH-01, ARCH-02 |
| **P2** | CONV-05, FMT-02~03, CFG-01~02, REG-01~02 |
