# /review-ecb — ECB / OCP / SRP 리뷰 (수정 없음)

Phase: *(현재 브랜치)* | Layer: **project** | Track: **C2C**

## 목적

**코드 수정 없이** ECB, OCP, SRP 준수 여부를 리뷰한다.

## 참조

- `docs/spec/08-design-spec.md`
- `docs/spec/12-quality-checklist.md`
- `.cursorrules`

## 절차

1. **선언** — Phase / Layer / Track
2. **레이어 매핑 검증**

| 레이어 | 경로 | entity import 금지 대상 |
|--------|------|-------------------------|
| entity | `src/unit_converter/entity/` | — |
| control | `src/unit_converter/control/` | boundary import 최소화 |
| boundary | `src/unit_converter/boundary/` | — |
| infrastructure | `src/unit_converter/infrastructure/` | entity 비즈니스 로직 금지 |

3. **의존 방향** — boundary → control → entity 다이어그램 대조
4. **OCP**
   - 새 Formatter → Converter 수정 불필요?
   - units.json 단위 추가 → Converter 수정 불필요?
5. **SRP** — Parser / Registry / Converter / Formatter / UseCase / CLI 분리
6. **Converter 규칙**
   - meter 경유 only
   - 단위별 if/elif 없음
7. **판정** — Pass / Fail per 항목 + 근거 (파일:줄)

## 금지

- **소스 수정**
- 테스트 수정

## 완료 보고 (한국어)

| 항목 | Pass/Fail | 근거 |
|------|-----------|------|
| ECB 의존 방향 | | |
| entity isolation | | |
| OCP | | |
| SRP | | |
| Converter 규칙 | | |

- 종합 판정, `/refactor-safe` 필요 항목
