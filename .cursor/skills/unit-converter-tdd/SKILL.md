---
name: unit-converter-tdd
description: >-
  UnitConverter_14 Dual-Track TDD (Logic/UI) with ECB layers and C2C traceability.
  Use when writing RED tests, minimal GREEN code, refactoring, or reviewing
  converter/registry/parser/formatter work. Triggers on TDD, RED, GREEN, REFACTOR,
  CONV, VAL, FMT, ECB, pytest, or unit-converter phases.
---

# UnitConverter TDD Skill

UnitConverter_14 길이 단위 변환 CLI의 **Dual-Track TDD + ECB + C2C** 워크플로.

## 작업 시작 선언

```
Phase: {spec|red|green|refactoring|new_features} | Layer: {entity|control|boundary|infrastructure} | Track: {Logic|UI|C2C}
```

## ARRR ↔ Phase

| ARRR | Phase | 브랜치 |
|------|-------|--------|
| Ask | red | `red` |
| Respond | green | `green` |
| Refine | refactoring | `refactoring` |
| Repeat | spec 갱신 → red | `spec` → `new_features` |

## Logic Track vs UI Track

| | Logic Track | UI Track |
|---|-------------|----------|
| **목적** | 도메인·InputParser 단위 | CLI E2E·포맷 |
| **Harness** | `tests/entity/`, `tests/control/`, `tests/boundary/test_input_parser.py` | `tests/boundary/test_cli.py` 등 |
| **ECB** | entity, control, boundary(parse) | boundary(E2E), infrastructure |
| **Test ID** | `CONV-*`, `VAL-*` (Logic assert) | `FMT-*`, `CLI-*`, `CFG-*`, `REG-*` |
| **VAL assert** | `ParseError` / `ValidationError` | exit code + stderr (CLI-03, CLI-04) |
| **Mock** | **Domain Mock 금지** | **허용** (stdin/stdout, 파일, CLI) |
| **RED 시 src/** | 수정 금지 | 수정 금지 |
| **참조 spec** | `06-conversion-rules.md`, `05-validation-spec.md` | `04-io-contract.md`, `03-functional-spec.md` |

## RED 절차

1. Phase/Layer/Track 선언
2. `docs/spec/09-scenario-catalog.md`에서 Test ID 확인
3. `docs/spec/11-traceability-matrix.md`에서 PRD ↔ CODE-REF 확인
4. **Logic:** `tests/entity/`, `tests/control/`, 또는 `tests/boundary/test_input_parser.py`
5. **UI:** `tests/boundary/`에 테스트 파일 추가
6. 본문은 **`pytest.fail("RED: Test ID {ID} — {Given-When-Then 요약}")` 만**
7. `src/` **수정 금지**
8. `pytest` 실행 → **FAILED** 확인

### RED 금지

- `skip`, `xfail`, assert 완화, 빈 `pass`
- Logic Track에서 Converter/Validator/Registry Mock
- GREEN 구현을 RED와 동시에 작성

## GREEN 절차

1. Phase/Layer/Track 선언
2. **RED 1묶음**(동일 TODO-ID)만 green으로
3. `docs/spec/08-design-spec.md` ECB CODE-REF 경로에 맞게 **최소** 구현
4. `pytest` 해당 Test ID → **PASSED**
5. 다른 RED 테스트는 여전히 FAIL 가능

### GREEN 금지

- RED에 없는 기능 추가
- REFACTOR 수준 구조 변경 (UseCase 분리 등은 refactoring에서)
- `converter.py` 단위별 if/elif

## REFACTOR 절차

1. **전체 P0 pytest green** 확인 후 착수
2. `refactor-smell` → `refactor-safe` 순서 권장
3. ECB 의존 방향 검증: boundary → control → entity
4. Test ID·assert **변경 금지**
5. REFACTOR 후 `pytest` 전체 green

## pytest 실행 규칙

```bash
# 가상환경 활성화 후
pytest                          # 전체
pytest tests/entity/ -v         # Logic Track
pytest tests/control/ -v
pytest tests/boundary/ -v       # UI Track
pytest -k "CONV-01" -v          # Test ID (이름/docstring에 포함 시)
```

| Phase | 기대 결과 |
|-------|-----------|
| RED | 해당 Test ID **FAILED** (`pytest.fail` 메시지) |
| GREEN | 해당 Test ID **PASSED** |
| REFACTOR | P0 전부 **PASSED** |

## ECB Quick Reference

```
boundary → control → entity
entity ✗→ boundary | control | infrastructure
```

| 레이어 | 경로 | 핵심 |
|--------|------|------|
| entity | `src/unit_converter/entity/` | Converter, Validator, UnitRegistry |
| control | `src/unit_converter/control/` | ConvertUseCase |
| boundary | `src/unit_converter/boundary/` | CLI, InputParser, Formatter |
| infrastructure | `src/unit_converter/infrastructure/` | ConfigLoader, UnitRegistrar |

## 완료 보고 항목

작업 종료 시 **한국어**로 아래를 보고한다.

1. **선언:** Phase | Layer | Track
2. **Test ID:** 처리한 ID 목록
3. **변경 파일:** 경로 목록
4. **pytest 결과:** PASS / FAIL / RED(의도적 실패)
5. **ECB 준수:** 위반 여부 (해당 시)
6. **다음 단계:** 제안 1줄 (선택)

## 상세 참조

- [reference.md](./reference.md) — Test ID, CODE-REF, 금지 패턴, C2C 프롬프트

## Commands

| Command | 용도 |
|---------|------|
| `/tdd-red` | RED 테스트만 |
| `/green-minimal` | 최소 GREEN |
| `/refactor-smell` | 스멜 탐지 (코드 수정 없음) |
| `/refactor-safe` | 안전 리팩터 |
| `/review-ecb` | ECB/OCP/SRP 리뷰 (코드 수정 없음) |
| `/export-session` | Report/Prompting 문서화 |
