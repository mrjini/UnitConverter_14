# 11 — Traceability Matrix (추적 매트릭스)

> PRD → TODO → Test ID → CODE-REF

---

## P0 — MVP

| PRD-ID | 요구 요약 | TODO-ID | 브랜치 | Test ID | CODE-REF |
|--------|-----------|---------|--------|---------|----------|
| PRD-001 | 모든 단위로 변환 출력 | TODO-001 | red→green | CONV-01~03, CLI-02 | `Converter.convert_all()` |
| PRD-002 | meter, feet, yard | TODO-002 | red→green | CONV-01~03 | `UnitRegistry` (default) |
| PRD-003 | README 비율 | TODO-003 | red→green | CONV-01 | `UnitRegistry` factors |
| PRD-004 | meter 경유 | TODO-004 | red→green | CONV-04 | `Converter._to_meters()`, `_from_meters()` |
| PRD-005 | 음수 거부 | TODO-005 | red→green | VAL-01, VAL-05 | `Validator.validate()` |
| PRD-006 | 형식 검증 | TODO-006 | red→green | VAL-02, VAL-02b, VAL-04 | `InputParser.parse()`, `Validator` |
| PRD-007 | 미등록 단위 | TODO-007 | red→green | VAL-03 | `UnitRegistry.get()`, `Validator` |
| PRD-008 | table 출력 | TODO-008 | red→green | FMT-01 | `TableFormatter.format()` |
| PRD-009 | 1자리 반올림 | TODO-009 | red→green | CONV-01 | `Converter` (display round) |

---

## P1 — 구조

| PRD-ID | 요구 요약 | TODO-ID | 브랜치 | Test ID | CODE-REF |
|--------|-----------|---------|--------|---------|----------|
| PRD-010 | OCP | TODO-010 | refactoring | (기존 CONV/FMT green 유지) | `Formatter` Protocol |
| PRD-011 | SRP | TODO-011 | refactoring | (기존 테스트 green) | 패키지 분리 §08 |
| PRD-012 | 추적성 | TODO-012 | spec | (본 문서) | — |
| — | CLI help | TODO-013 | green | CLI-01 | `cli.main()` |

---

## P2 — 확장

| PRD-ID | 요구 요약 | TODO-ID | 브랜치 | Test ID | CODE-REF |
|--------|-----------|---------|--------|---------|----------|
| PRD-013 | 설정 파일 | TODO-014 | new_features | CFG-01, CFG-02 | `ConfigLoader.load()` |
| PRD-014 | cubit 동적 등록 | TODO-015 | new_features | REG-01, REG-02, CONV-05 | `UnitRegistrar.register()` |
| PRD-015 | json 출력 | TODO-016 | new_features | FMT-02 | `JsonFormatter.format()` |
| PRD-016 | csv 출력 | TODO-017 | new_features | FMT-03 | `CsvFormatter.format()` |
| PRD-017 | table 옵션 | TODO-018 | new_features | FMT-01 | `cli` format arg |

---

## Mom Test → 추적

| Mom Test 증거 | PRD | Test ID |
|---------------|-----|---------|
| feet/yard 상수 불일치 40분 | PRD-004 | CONV-04 |
| 형식 검증 누락 | PRD-006 | VAL-02, VAL-04 |
| 수동 비교표 1시간 | PRD-012, SC-5 | 전체 pytest |

---

## Orphan 검사 규칙

| 유형 | 규칙 |
|------|------|
| PRD | 모든 PRD-ID ≥ 1 Test ID |
| Test ID | 모든 P0/P2 Test ID ≥ 1 PRD-ID |
| TODO | 모든 TODO ≥ 1 PRD, RED/GREEN 브랜치 지정 |
| CODE-REF | GREEN 완료 시 구현 경로 기록 (REFACTOR에서 갱신) |

**SC-1:** merge 전 orphan **0건**

---

## TODO 백로그 (RED 착수용)

| TODO-ID | 설명 | 브랜치 | 상태 |
|---------|------|--------|------|
| TODO-001 | CONV-01~03 RED 테스트 | red | pending |
| TODO-004 | CONV-04 meter 경유 RED | red | pending |
| TODO-005~007 | VAL-* RED 테스트 | red | pending |
| TODO-008 | FMT-01 RED | red | pending |
| TODO-013 | CLI-02 E2E RED | red | pending |
| TODO-010~011 | SRP/OCP 리팩터 | refactoring | pending |
| TODO-014~018 | P2 확장 | new_features | pending |
