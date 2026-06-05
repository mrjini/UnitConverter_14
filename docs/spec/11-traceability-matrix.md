# 11 — Traceability Matrix (추적 매트릭스)

> PRD → TODO → Test ID → CODE-REF (ECB 경로)

**CODE-REF 표기:** `{layer}.{module}.{Class}.{method}` — `src/unit_converter/{layer}/` 기준

---

## P0 — MVP

| PRD-ID | 요구 요약 | TODO-ID | 브랜치 | Test ID | ECB | CODE-REF |
|--------|-----------|---------|--------|---------|-----|----------|
| PRD-001 | 모든 단위로 변환 출력 | TODO-001 | red→green | CONV-01~03, CLI-02 | entity, control | `entity.converter.Converter.convert_all()` |
| PRD-002 | meter, feet, yard | TODO-002 | red→green | CONV-01~03 | entity | `entity.registry.UnitRegistry` |
| PRD-003 | README 비율 | TODO-003 | red→green | CONV-01 | entity | `entity.registry.Unit.to_meter_factor` |
| PRD-004 | meter 경유 | TODO-004 | red→green | CONV-04 | entity | `entity.converter.Converter._to_meters()`, `_from_meters()` |
| PRD-005 | 음수 거부 | TODO-005 | red→green | VAL-01, VAL-05, CLI-03 | entity, boundary | `entity.validator.Validator.validate()`, `boundary.cli` |
| PRD-006 | 형식 검증 | TODO-006 | red→green | VAL-02, VAL-02b, VAL-04, CLI-04 | boundary | `boundary.input_parser.InputParser.parse()` |
| PRD-007 | 미등록 단위 | TODO-007 | red→green | VAL-03 | entity | `entity.validator.Validator.validate()` |
| PRD-008 | table 출력 | TODO-008 | red→green | FMT-01 | boundary | `boundary.formatter.table.TableFormatter.format()` |
| PRD-009 | 1자리 반올림 | TODO-009 | red→green | CONV-01 | entity | `entity.converter.Converter` (display round) |
| — | 유스케이스 조율 | TODO-001b | red→green | CONV-* (control) | control | `control.convert_use_case.ConvertUseCase.execute(unit, value, registry)` |

---

## P1 — 구조

| PRD-ID | 요구 요약 | TODO-ID | 브랜치 | Test ID | ECB | CODE-REF |
|--------|-----------|---------|--------|---------|-----|----------|
| PRD-010 | OCP | TODO-010 | refactoring | ARCH-01 | boundary | `boundary.formatter.base.Formatter` Protocol |
| PRD-011 | SRP / ECB | TODO-011 | refactoring | ARCH-02 | 전 레이어 | ECB §08-design-spec |
| PRD-012 | 추적성 | TODO-012 | spec | (meta) | — | `11-traceability-matrix.md` |
| — | CLI help | TODO-013 | green | CLI-01 | boundary | `boundary.cli.main()` |

> **PRD-012 (meta):** Test ID 대신 추적 매트릭스 orphan 검사로 수용. pytest ID 불필요.

---

## P2 — 확장

| PRD-ID | 요구 요약 | TODO-ID | 브랜치 | Test ID | ECB | CODE-REF |
|--------|-----------|---------|--------|---------|-----|----------|
| PRD-013 | 설정 파일 | TODO-014 | new_features | CFG-01, CFG-02 | infrastructure | `infrastructure.config_loader.ConfigLoader.load()` |
| PRD-014 | cubit 동적 등록 | TODO-015 | new_features | REG-01, REG-02, CONV-05 | infrastructure, control | `infrastructure.unit_registrar`, `control.register_unit_use_case` |
| PRD-015 | json 출력 | TODO-016 | new_features | FMT-02 | boundary | `boundary.formatter.json_fmt.JsonFormatter.format()` |
| PRD-016 | csv 출력 | TODO-017 | new_features | FMT-03 | boundary | `boundary.formatter.csv_fmt.CsvFormatter.format()` |
| PRD-017 | table 옵션 | TODO-018 | new_features | FMT-01 | boundary | `boundary.cli` (`--format`) |

---

## ECB 레이어 ↔ Test Harness

| ECB | Harness (tests) | Test 접두 |
|-----|-----------------|-----------|
| entity | `tests/entity/` | CONV-*, VAL-01, VAL-03, VAL-05 |
| control | `tests/control/` | ConvertUseCase |
| boundary (단위) | `tests/boundary/test_input_parser.py` | VAL-02, VAL-02b, VAL-04 |
| boundary (E2E) | `tests/boundary/test_cli.py` 등 | FMT-*, CLI-* |
| infrastructure | `tests/boundary/` (E2E) | CFG-*, REG-* |

---

## Mom Test → 추적

| Mom Test 증거 | PRD | Test ID | ECB |
|---------------|-----|---------|-----|
| feet/yard 상수 불일치 40분 | PRD-004 | CONV-04 | entity |
| 형식 검증 누락 | PRD-006 | VAL-02, VAL-04, CLI-04 | boundary |
| 수동 비교표 1시간 | PRD-012, SC-5 | 전체 pytest | 전 레이어 |

---

## Orphan 검사 규칙

| 유형 | 규칙 |
|------|------|
| PRD | P0/P2 PRD ≥ 1 Test ID. **예외:** PRD-012 (meta, 매트릭스 자체) |
| Test ID | P0/P2 Test ID ≥ 1 PRD-ID. P1 ARCH-* ≥ 1 PRD-ID |
| TODO | 모든 TODO ≥ 1 PRD, RED/GREEN 브랜치 지정, **ID 유일** |
| CODE-REF | `{layer}.{module}` 형식 |

**SC-1:** merge 전 orphan **0건** (PRD-012 제외)

---

## TODO 백로그 (RED 착수용)

| TODO-ID | 설명 | ECB | Harness | 브랜치 | 상태 |
|---------|------|-----|---------|--------|------|
| TODO-001 | CONV-01~03 RED | entity | tests/entity | red | pending |
| TODO-001b | ConvertUseCase RED | control | tests/control | red | pending |
| TODO-004 | CONV-04 RED | entity | tests/entity | red | pending |
| TODO-005 | VAL-01, VAL-05 RED | entity | tests/entity | red | pending |
| TODO-006 | VAL-02, 02b, 04 RED | boundary | tests/boundary/test_input_parser | red | pending |
| TODO-007 | VAL-03 RED | entity | tests/entity | red | pending |
| TODO-008 | FMT-01 RED | boundary | tests/boundary | red | pending |
| TODO-013 | CLI-01 help RED | boundary | tests/boundary | green | pending |
| TODO-019 | CLI-02~04 E2E RED | boundary | tests/boundary | red | pending |
| TODO-010~011 | ECB/OCP 리팩터 | 전 레이어 | — | refactoring | pending |
| TODO-014~018 | P2 확장 | infra, boundary | tests/boundary | new_features | pending |
