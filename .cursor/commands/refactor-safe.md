# /refactor-safe — 테스트 green 유지 안전 리팩터

Phase: **refactoring** | Layer: **project** | Track: **C2C**

## 목적

**pytest P0 전부 PASS** 상태에서 구조만 개선. Test ID·assert 의미 **불변**.

## 전제

- REFACTOR 착수 전: `pytest` P0 green
- `/refactor-smell` 결과 있으면 우선순위 반영
- Skill: `.cursor/skills/unit-converter-tdd/SKILL.md`

## 절차

1. **선언** — Phase / Layer / Track
2. **사전 pytest** — `pytest tests/entity/ tests/control/ tests/boundary/ -v` → green 확인
3. **리팩터 범위** — ECB 레이어 정렬, SRP 분리, Formatter Protocol 등
4. **금지 패턴 제거**
   - converter if/elif → Registry + meter 경유
   - entity → boundary import 제거
5. **Test ID·시나리오 assert 변경 금지**
6. **사후 pytest** — 동일 명령 → **전부 green**
7. 실패 시 **즉시 롤백** 후 원인 보고

## 허용

- 파일·클래스 이동 (ECB 경로 정렬)
- private 메서드 추출 (`_to_meters`, `_from_meters`)
- import 정리, 타입 힌트

## 금지

- Test ID rename
- assert 기대값 변경 (Golden Values 유지)
- 기능 추가 (new_features에서)

## 완료 보고 (한국어)

- 리팩터 항목, 변경 파일, pytest before/after
- `/review-ecb` 권장 여부
