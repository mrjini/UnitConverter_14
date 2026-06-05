# /green-minimal — RED 1묶음 최소 구현

Phase: **green** | Layer: *(entity|control|boundary|infrastructure)* | Track: *(Logic|UI|C2C)*

## 목적

지정된 **RED 1묶음**(동일 TODO-ID 또는 사용자 지정 Test ID 묶음)만 통과시키는 **최소** 구현.

## 전제

- 해당 RED 테스트가 `pytest.fail("RED: ...")` 상태
- Skill: `.cursor/skills/unit-converter-tdd/SKILL.md`

## 절차

1. **선언** — Phase / Layer / Track
2. **범위 고정** — Test ID 1묶음만 (예: CONV-01~03, 또는 VAL-01 단독)
3. **ECB CODE-REF** — `docs/spec/08-design-spec.md`, `docs/spec/11-traceability-matrix.md`
4. **최소 구현** — 해당 레이어에만 코드 추가
   - entity: Registry, Validator, Converter (meter 경유, if/elif 단위 분기 금지)
   - control: ConvertUseCase
   - boundary: CLI, InputParser, Formatter
   - infrastructure: ConfigLoader, UnitRegistrar
5. **RED 테스트 본문 교체** — `pytest.fail` → 실제 assert (해당 묶음만)
6. **실행** — `pytest -k "{묶음}" -v` → **PASSED**
7. **범위 외 RED** — 여전히 FAIL이어도 됨

## 금지

- RED에 없는 Test ID 구현
- REFACTOR 수준 패키지 대수술
- `converter.py` 단위별 if/elif
- 새 단위 추가를 위해 converter.py 수정

## 완료 보고 (한국어)

- Test ID, 변경 src/tests 파일, pytest PASSED/FAIL 목록
- ECB 위반 여부
