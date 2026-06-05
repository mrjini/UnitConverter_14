# /tdd-red — RED 테스트만 작성

Phase: **red** | Layer: *(entity|control|boundary)* | Track: *(Logic|UI)*

## 목적

Given-When-Then 시나리오에 맞는 **실패 테스트만** 추가한다. 구현은 하지 않는다.

## 전제

- Skill: `.cursor/skills/unit-converter-tdd/SKILL.md` 준수
- `.cursorrules` RED 규칙 준수

## 절차

1. **선언** — Phase / Layer / Track (응답 첫 줄)
2. **Test ID 확인** — `docs/spec/09-scenario-catalog.md`, `docs/spec/11-traceability-matrix.md`
3. **파일 위치**
   - Logic — entity: `CONV-*`, `VAL-01`, `VAL-03`, `VAL-05` → `tests/entity/`
   - Logic — control: `ConvertUseCase` → `tests/control/`
   - Logic — parse: `VAL-02`, `VAL-02b`, `VAL-04` → `tests/boundary/test_input_parser.py`
   - UI — E2E: `FMT-*`, `CLI-*`, `CFG-*`, `REG-*` → `tests/boundary/`
4. **Logic VAL:** exit code assert 금지 — `ParseError` / `ValidationError`만 (UI는 CLI-03, CLI-04)
5. **테스트 작성**
   - test 함수명·docstring에 Test ID 포함
   - 본문: **`pytest.fail("RED: Test ID {ID} — {요약}")` 만**
6. **`src/` 수정 금지** — `src/unit_converter/` 포함
7. **실행** — `pytest -k "{Test ID}" -v` → **FAILED** 확인

## 금지

| 항목 | |
|------|---|
| `src/` 구현 코드 | ✗ |
| `@pytest.mark.skip` / `xfail` | ✗ |
| assert 완화·try/except 우회 | ✗ |
| Logic Track Domain Mock | ✗ |
| GREEN 코드 동시 작성 | ✗ |

## 완료 보고 (한국어)

- Test ID, 변경 테스트 파일, pytest FAILED 결과
- 다음: `/green-minimal` 대상 Test ID 1줄
