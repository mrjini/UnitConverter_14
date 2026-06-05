# /refactor-smell — 코드 스멜 탐지 (수정 없음)

Phase: **refactoring** | Layer: **project** | Track: **C2C**

## 목적

**코드를 수정하지 않고** ECB / SRP / OCP / TDD 스멜만 탐지·보고한다.

## 전제

- `.cursorrules`, `docs/spec/08-design-spec.md`, `docs/spec/12-quality-checklist.md`

## 절차

1. **선언** — Phase / Layer / Track
2. **스캔 대상** — `src/unit_converter/`, `tests/`, `UnitConverter.py`
3. **체크리스트**

### ECB

- [ ] boundary → control → entity 의존 방향
- [ ] entity가 boundary/control/infrastructure import 하는지
- [ ] CLI가 entity 직접 호출 (control 우회) 하는지

### Converter / OCP

- [ ] `converter.py` 단위별 if/elif
- [ ] feet↔yard 직접 상수
- [ ] 새 단위 추가 시 converter 변경 필요 구조

### SRP

- [ ] Parser / Registry / Converter / Formatter / UseCase / CLI 혼재
- [ ] 한 파일·한 클래스 다중 변경 이유

### TDD / Test

- [ ] Logic Track Domain Mock 사용
- [ ] skip/xfail 남용
- [ ] Test ID ↔ PRD orphan

4. **출력** — 심각도(High/Medium/Low), 파일:줄, 스멜 설명, 권장 조치 (코드 없음)

## 금지

- **어떤 소스 파일도 수정하지 않음**
- 자동 리팩터 수행

## 완료 보고 (한국어)

- 스멜 목록 표 (심각도, 위치, 설명)
- `/refactor-safe` 우선순위 제안
