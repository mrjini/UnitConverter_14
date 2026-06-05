# 12 — Quality Checklist (품질 체크리스트)

## SPEC → staging merge 게이트

### 문서 완성도

- [ ] 00-glossary 용어 일관
- [ ] 02-prd 모든 요구 PRD-ID 부여
- [ ] 09-scenario-catalog P0 시나리오 Given-When-Then 완료
- [ ] 11-traceability-matrix orphan 0건
- [ ] 06-conversion-rules Golden Values (8.2, 2.7) 명시

### SPEC 금지사항 준수

- [ ] 구현 코드 추가/수정 없음 (`UnitConverter.py` 불변)
- [ ] pytest / RED 테스트 없음
- [ ] units.json 실 파일 없음

---

## RED → GREEN 게이트

- [ ] P0 Test ID 전부 RED (실패) 확인
- [ ] Test 함수/docstring에 Test ID 명시
- [ ] Track A 테스트가 Converter/Validator만 직접 호출 (CLI 미의존)

---

## GREEN → REFACTORING 게이트

- [ ] P0 pytest 전부 green
- [ ] feet↔yard 직접 상수 코드에 없음 (CONV-04)
- [ ] exit code VAL-* = 1

---

## REFACTORING → staging 게이트

### SRP

- [ ] InputParser: 파싱만
- [ ] Validator: 검증만
- [ ] Converter: 변환만
- [ ] Formatter: 출력만
- [ ] CLI: 오케스트레이션만

### OCP

- [ ] 새 Formatter 추가 시 Converter 수정 없음
- [ ] units.json 단위 추가 시 Converter 수정 없음

### 회귀

- [ ] REFACTOR 후 P0 Test ID 전부 green
- [ ] Test ID 변경 없음

---

## new_features → staging 게이트

- [ ] P2 Test ID (CFG, REG, FMT-02/03) green
- [ ] PRD-013~017 추적 매트릭스 CODE-REF 갱신
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
