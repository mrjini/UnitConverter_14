# 09 — Scenario Catalog (시나리오 카탈로그)

> Given-When-Then 형식. **pytest 코드 없음** — RED 단계에서 구현.

## ECB ↔ Track ↔ Harness

| Track | ECB | Test Harness | Test 접두 |
|-------|-----|--------------|-----------|
| A | entity | `tests/entity/` | CONV-*, VAL-* |
| A | control | `tests/control/` | ConvertUseCase |
| B | boundary | `tests/boundary/` | FMT-*, CLI-* |
| B | infrastructure (E2E) | `tests/boundary/` | CFG-*, REG-* |

---

## Track A — entity / control

### CONV — 변환

#### CONV-01: meter 입력 기본 변환

| | |
|---|---|
| **Given** | Registry에 meter, feet, yard 등록 |
| **When** | `meter:2.5` 변환 |
| **Then** | meter=2.5, feet=8.2, yard=2.7 (1자리) |
| **PRD** | PRD-001, 003, 008, 009 |
| **ECB** | entity (`entity.converter`) |

#### CONV-02: feet 입력 변환

| | |
|---|---|
| **Given** | Registry 기본 3단위 |
| **When** | `feet:8.2` 변환 |
| **Then** | meter≈2.5, feet=8.2, yard 출력 (meter 경유) |
| **PRD** | PRD-001, 004 |

#### CONV-03: yard 입력 변환

| | |
|---|---|
| **Given** | Registry 기본 3단위 |
| **When** | `yard:2.7` 변환 |
| **Then** | meter, feet, yard 모두 출력 |
| **PRD** | PRD-001, 004 |

#### CONV-04: meter 경유 일관성 (feet→yard)

| | |
|---|---|
| **Given** | Registry 기본 3단위 |
| **When** | `feet:3.28084` 변환 |
| **Then** | yard 결과 = `1.0` (1 feet = 1/3.28084 m → 1 yard) |
| **PRD** | PRD-004 |
| **Note** | 직접 feet→yard 상수 사용 시 **실패**해야 함 |

#### CONV-05: cubit 포함 변환 [P2]

| | |
|---|---|
| **Given** | cubit 등록 (0.4572 m) |
| **When** | `cubit:1` 변환 |
| **Then** | meter=0.5 (1자리), feet/yard/cubit 출력 |
| **PRD** | PRD-014 |

---

### VAL — 검증

#### VAL-01: 음수 거부

| | |
|---|---|
| **Given** | Registry 기본 |
| **When** | `meter:-1` |
| **Then** | ERR_NEGATIVE, exit 1 |
| **PRD** | PRD-005 |

#### VAL-02: 형식 오류 — 콜론 없음

| | |
|---|---|
| **Given** | — |
| **When** | `meter2.5` |
| **Then** | ERR_FORMAT, exit 1 |
| **PRD** | PRD-006 |

#### VAL-02b: 숫자 오류

| | |
|---|---|
| **Given** | — |
| **When** | `meter:abc` |
| **Then** | ERR_NUMBER, exit 1 |
| **PRD** | PRD-006 |

#### VAL-03: 미등록 단위

| | |
|---|---|
| **Given** | Registry 기본 |
| **When** | `mile:1` |
| **Then** | ERR_UNKNOWN_UNIT, exit 1 |
| **PRD** | PRD-007 |

#### VAL-04: 빈 값

| | |
|---|---|
| **Given** | — |
| **When** | `meter:` |
| **Then** | ERR_FORMAT, exit 1 |
| **PRD** | PRD-006 |

#### VAL-05: 영 허용

| | |
|---|---|
| **Given** | Registry 기본 |
| **When** | `feet:0` |
| **Then** | exit 0, 모든 단위 0 |
| **PRD** | PRD-005 |

---

## Track B — boundary / infrastructure

### FMT — 출력 포맷

#### FMT-01: table 기본 [P0]

| | |
|---|---|
| **Given** | format=table (default) |
| **When** | `meter:2.5` |
| **Then** | 3줄, `{v} {unit} = {tv} {tunit}` 형식 |
| **PRD** | PRD-008 |

#### FMT-02: json [P2]

| | |
|---|---|
| **Given** | `--format json` |
| **When** | `meter:2.5` |
| **Then** | valid JSON array, 필드 io-contract 준수 |
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

#### REG-02: 잘못된 등록 [P2]

| | |
|---|---|
| **Given** | — |
| **When** | `--register "bad"` |
| **Then** | ERR_REGISTRATION, exit 2 |
| **PRD** | PRD-014 |

---

### CLI — 통합

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

---

## 우선순위 요약

| Priority | Test IDs |
|:--------:|----------|
| **P0** | CONV-01~04, VAL-01~05, FMT-01, CLI-02 |
| **P1** | CLI-01, PRD-010~012 (설계 검증) |
| **P2** | CONV-05, FMT-02~03, CFG-01~02, REG-01~02 |
