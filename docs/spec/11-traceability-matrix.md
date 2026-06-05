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
| PRD-005 | 음수 거부 | TODO-005 | red→green | VAL-01, VAL-05 | entity | `entity.validator.Validator.validate()` |
| PRD-006 | 형식 검증 | TODO-006 | red→green | VAL-02, VAL-02b, VAL-04 | boundary, entity | `boundary.input_parser.InputParser.parse()`, `entity.validator.Validator` |
| PRD-007 | 미등록 단위 | TODO-007 | red→green | VAL-03 | entity | `entity.registry.UnitRegistry.get()`, `entity.validator.Validator` |
| PRD-008 | table 출력 | TODO-008 | red→green | FMT-01 | boundary | `boundary.formatter.table.TableFormatter.format()` |
| PRD-009 | 1자리 반올림 | TODO-009 | red→green | CONV-01 | entity | `entity.converter.Converter` (display round) |
| — | 유스케이스 조율 | TODO-001b | red→green | CONV-*, CLI-02 | control | `control.convert_use_case.ConvertUseCase.execute()` |

---

## P1 — 구조

| PRD-ID | 요구 요약 | TODO-ID | 브랜치 | Test ID | ECB | CODE-REF |
|--------|-----------|---------|--------|---------|-----|----------|
| PRD-010 | OCP | TODO-010 | refactoring | (CONV/FMT green 유지) | boundary | `boundary.formatter.base.Formatter` Protocol |
| PRD-011 | SRP / ECB | TODO-011 | refactoring | (기존 green) | 전 레이어 | ECB 패키지 §08-design-spec |
| PRD-012 | 추적성 | TODO-012 | spec | (본 문서) | — | — |
| — | CLI help | TODO-013 | green | CLI-01 | boundary | `boundary.cli.main()` |

---

## P2 — 확장

| PRD-ID | 요구 요약 | TODO-ID | 브랜치 | Test ID | ECB | CODE-REF |
|--------|-----------|---------|--------|---------|-----|----------|
| PRD-013 | 설정 파일 | TODO-014 | new_features | CFG-01, CFG-02 | infrastructure | `infrastructure.config_loader.ConfigLoader.load()` |
| PRD-014 | cubit 동적 등록 | TODO-015 | new_features | REG-01, REG-02, CONV-05 | infrastructure, control | `infrastructure.unit_registrar.UnitRegistrar`, `control.register_unit_use_case` |
| PRD-015 | json 출력 | TODO-016 | new_features | FMT-02 | boundary | `boundary.formatter.json_fmt.JsonFormatter.format()` |
| PRD-016 | csv 출력 | TODO-017 | new_features | FMT-03 | boundary | `boundary.formatter.csv_fmt.CsvFormatter.format()` |
| PRD-017 | table 옵션 | TODO-018 | new_features | FMT-01 | boundary | `boundary.cli` (`--format`) |

---

## ECB 레이어 ↔ Test Harness

| ECB | Harness (src) | Harness (tests) | Test 접두 |
|-----|---------------|-----------------|-----------|
| entity | `src/unit_converter/entity/` | `tests/entity/` | CONV-*, VAL-* |
| control | `src/unit_converter/control/` | `tests/control/` | UseCase, CLI-02 unit |
| boundary | `src/unit_converter/boundary/` | `tests/boundary/` | FMT-*, CLI-* |
| infrastructure | `src/unit_converter/infrastructure/` | `tests/boundary/` (E2E) | CFG-*, REG-* |

---

## Mom Test → 추적

| Mom Test 증거 | PRD | Test ID | ECB |
|---------------|-----|---------|-----|
| feet/yard 상수 불일치 40분 | PRD-004 | CONV-04 | entity |
| 형식 검증 누락 | PRD-006 | VAL-02, VAL-04 | boundary + entity |
| 수동 비교표 1시간 | PRD-012, SC-5 | 전체 pytest | 전 레이어 |

---

## Orphan 검사 규칙

| 유형 | 규칙 |
|------|------|
| PRD | 모든 PRD-ID ≥ 1 Test ID |
| Test ID | 모든 P0/P2 Test ID ≥ 1 PRD-ID, ECB 레이어 지정 |
| TODO | 모든 TODO ≥ 1 PRD, RED/GREEN 브랜치 지정 |
| CODE-REF | `{layer}.{module}` 형식, GREEN 완료 시 경로 기록 |

**SC-1:** merge 전 orphan **0건**

---

## TODO 백로그 (RED 착수용)

| TODO-ID | 설명 | ECB | Harness | 브랜치 | 상태 |
|---------|------|-----|---------|--------|------|
| TODO-001 | CONV-01~03 RED | entity | tests/entity | red | pending |
| TODO-001b | ConvertUseCase RED | control | tests/control | red | pending |
| TODO-004 | CONV-04 meter 경유 RED | entity | tests/entity | red | pending |
| TODO-005~007 | VAL-* RED | entity | tests/entity | red | pending |
| TODO-008 | FMT-01 RED | boundary | tests/boundary | red | pending |
| TODO-013 | CLI-02 E2E RED | boundary | tests/boundary | red | pending |
| TODO-010~011 | ECB/OCP 리팩터 | 전 레이어 | — | refactoring | pending |
| TODO-014~018 | P2 확장 | infra, boundary | tests/boundary | new_features | pending |
