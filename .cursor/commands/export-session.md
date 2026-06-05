# /export-session — Report / Prompting 문서화

Phase: *(현재)* | Layer: **harness** | Track: **C2C**

## 목적

현재 세션의 TDD·ECB·AI 활용 내용을 `Report/`, `Prompting/`에 문서로 남긴다.

## 전제

- **구현 코드·RED 테스트 본문 작성 금지** (spec/red 초기 Harness 단계에서는 템플릿·메타만)
- 사용자가 명시적으로 export 요청한 경우에만 파일 생성

## 출력 파일 (날짜 접두 권장)

| 파일 | 폴더 | 내용 |
|------|------|------|
| `YYYY-MM-DD-session.md` | `Report/` | Phase, Test ID, pytest 결과, ECB 판정, 회고 |
| `YYYY-MM-DD-prompts.md` | `Prompting/` | 사용 Command, 프롬프트, ARRR 단계 |

## Report 템플릿

```markdown
# Session Report — YYYY-MM-DD

## 선언
Phase: | Layer: | Track:

## Test ID 진행
| ID | Phase | Result |
|----|-------|--------|

## pytest
- 명령:
- 결과:

## ECB / OCP / SRP
- Pass/Fail 요약

## Mom Test 연결
- 재검증 자동화 여부

## 회고
- 잘 된 점 / 개선점
```

## Prompting Template

```markdown
# Prompts — YYYY-MM-DD

## ARRR
- Ask (RED):
- Respond (GREEN):
- Refine (REFACTOR):
- Repeat:

## Commands Used
- /tdd-red
- ...

## Effective Prompts
1. ...

## Limits
- ...
```

## 절차

1. **선언** — Phase / Layer / Track
2. 세션 컨텍스트 수집 (Test ID, pytest, 변경 파일)
3. `Report/`, `Prompting/`에 markdown 작성
4. **git commit 하지 않음** (사용자 요청 시만)

## 완료 보고 (한국어)

- 생성된 파일 경로 목록만
