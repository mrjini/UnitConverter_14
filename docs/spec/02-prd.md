# 02 — PRD (Product Requirements Document)

## 개요

| 항목 | 내용 |
|------|------|
| **제품명** | UnitConverter_14 |
| **유형** | 길이 단위 변환 CLI (Python) |
| **목표** | PRD → To-Do → Test ID → Code 추적 가능한 C2C + Dual-Track TDD 구현 |
| **Mom Test 진짜 문제** | 변환값·검증 기준이 분산되어 상수/규칙 변경 시 매번 처음부터 수동 재검증 |

---

## 요구사항 목록

### P0 — MVP (red → green)

| PRD-ID | 우선순위 | 요구사항 | Mom Test / R-G-I-O 근거 |
|--------|:--------:|----------|-------------------------|
| **PRD-001** | P0 | 사용자가 `unit:value` 형식으로 길이를 입력하면, 등록된 **모든 단위**로 변환 결과를 출력한다. | 표면 문제 — 기본 CLI |
| **PRD-002** | P0 | 초기 지원 단위: `meter`, `feet`, `yard`. | README 기본 요구 |
| **PRD-003** | P0 | 변환 비율: `1 meter = 3.28084 feet`, `1 meter = 1.09361 yard`. | README 비즈니스 로직 |
| **PRD-004** | P0 | feet↔yard 및 임의 단위 쌍 변환은 **반드시 meter를 경유**한다. 직접 비율 상수 금지. | Mom Test — 40분 상수 불일치 방지 |
| **PRD-005** | P0 | 음수 값 입력 시 변환하지 않고 오류를 반환한다. | 품질 요구 — 입력 검증 |
| **PRD-006** | P0 | `unit:value` 형식 위반 시(콜론 없음, 빈 값 등) 오류를 반환한다. | Mom Test — 형식 검증 누락 |
| **PRD-007** | P0 | 등록되지 않은 단위 입력 시 오류를 반환한다. | 품질 요구 — 미등록 단위 |
| **PRD-008** | P0 | 기본 출력 포맷은 **table** (한 줄 per 변환). | README 출력 예시 |
| **PRD-009** | P0 | 출력 수치는 소수점 **1자리**, 반올림(round half up). | README `8.2`, `2.7` 예시 |

### P1 — 구조 (green → refactoring)

| PRD-ID | 우선순위 | 요구사항 | 근거 |
|--------|:--------:|----------|------|
| **PRD-010** | P1 | OCP: 새 단위·포맷 추가 시 Converter 핵심 로직 수정 없이 확장 가능. | 품질 요구 OCP |
| **PRD-011** | P1 | SRP + ECB: entity / control / boundary / infrastructure 역할 분리. | 품질 요구 SRP |
| **PRD-012** | P1 | 모든 PRD 요구는 Test ID와 1:1 이상 추적 가능. | SC-1 추적성 |

### P2 — 확장 (new_features)

| PRD-ID | 우선순위 | 요구사항 | 근거 |
|--------|:--------:|----------|------|
| **PRD-013** | P2 | 변환 비율을 외부 설정 파일(JSON 또는 YAML)에서 로드한다. | 추가 요구 — 설정 외부화 |
| **PRD-014** | P2 | 런타임에 `1 cubit = 0.4572 meter` 형태로 단위를 동적 등록한다. | 추가 요구 — 동적 등록 |
| **PRD-015** | P2 | `--format json` 옵션으로 JSON 배열 출력. | 추가 요구 — 출력 포맷 |
| **PRD-016** | P2 | `--format csv` 옵션으로 CSV 출력. | 추가 요구 — 출력 포맷 |
| **PRD-017** | P2 | `--format table` 옵션 (기본값). | 추가 요구 — 출력 포맷 |

---

## 비기능 요구

| ID | 요구 |
|----|------|
| NFR-001 | Python 3.10+ |
| NFR-002 | pytest 기반 테스트 |
| NFR-003 | 외부 의존성 최소 (표준 라이브러리 우선, YAML 시 PyYAML 허용) |
| NFR-004 | CLI 단일 진입점: `UnitConverter.py` → `boundary.cli.main()` |

---

## 수용 기준 (Acceptance)

PRD는 **SC-1~SC-5** ([01-rgio.md](./01-rgio.md)) 및 [11-traceability-matrix.md](./11-traceability-matrix.md)의 Test ID 통과로 수용한다.

---

## Out of Scope

- GUI / 웹 API
- 질량·온도 등 길이 외 물리량
- 다국어 UI
- 실시간 환율·동적 비율 API 연동
