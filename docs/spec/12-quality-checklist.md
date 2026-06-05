# 12 — Quality Checklist (품질 체크리스트)

## SPEC → staging merge 게이트

### 문서 완성도

- [ ] 00-glossary ECB 용어 일관
- [ ] 08-design-spec ECB 레이어·의존 방향 (boundary → control → entity)
- [ ] 02-prd 모든 요구 PRD-ID 부여
- [ ] 09-scenario-catalog P0 시나리오 Given-When-Then 완료
- [ ] 11-traceability-matrix orphan 0건, CODE-REF ECB 경로
- [ ] 06-conversion-rules Golden Values (8.2, 2.7) 명시

### SPEC 금지사항 준수

- [ ] `src/unit_converter/` — Harness(`__init__.py`)만, 구현 없음
- [ ] `tests/` — Harness만, RED/pytest 본문 없음
- [ ] `UnitConverter.py` 불변
- [ ] units.json 실 파일 없음

### Harness 존재

- [ ] `src/unit_converter/{entity,control,boundary,infrastructure}/`
- [ ] `tests/{entity,control,boundary}/`

---

## RED → GREEN 게이트

- [ ] P0 Test ID 전부 RED (실패) 확인
- [ ] Test 함수/docstring에 Test ID 명시
- [ ] `tests/entity/` — entity만 직접 호출 (CLI/boundary 미의존)
- [ ] `tests/control/` — ConvertUseCase 단위

---

## GREEN → REFACTORING 게이트

- [ ] P0 pytest 전부 green
- [ ] feet↔yard 직접 상수 `entity/`에 없음 (CONV-04)
- [ ] exit code VAL-* = 1

---

## REFACTORING → staging 게이트

### ECB / SRP

| 레이어 | 검증 |
|--------|------|
| **entity** | Validator, Converter, UnitRegistry — 도메인만 |
| **control** | ConvertUseCase — 조율만, I/O 없음 |
| **boundary** | CLI, InputParser, Formatter — 표현·I/O만 |
| **infrastructure** | ConfigLoader, UnitRegistrar — 외부 자원만 |

- [ ] entity → boundary 의존 **없음**
- [ ] entity → infrastructure 의존 **없음**
- [ ] boundary → control → entity 의존 방향 준수

### OCP

- [ ] 새 Formatter(boundary) 추가 시 entity.Converter 수정 없음
- [ ] units.json 단위 추가 시 entity.Converter 수정 없음

### 회귀

- [ ] REFACTOR 후 P0 Test ID 전부 green
- [ ] Test ID 변경 없음

---

## new_features → staging 게이트

- [ ] P2 Test ID (CFG, REG, FMT-02/03) green
- [ ] PRD-013~017 추적 매트릭스 CODE-REF (infrastructure/boundary) 갱신
- [ ] SPEC 문서(07, 09)와 구현 일치

---

## Mom Test 회귀 방지 (SC-5)

- [ ] 상수 변경 시 pytest 1회로 Go/No-Go 가능
- [ ] 수동 엑셀/검색 비교 불필요
- [ ] VAL-* + CONV-* CI(또는 로컬) 필수 실행

---

## 발표/회고 (Activities 5)

- [ ] 추적 매트릭스 스크린샷 또는 링크
- [ ] ARRR 사이클 1회 이상 기록
- [ ] AI 활용 회고 메모
