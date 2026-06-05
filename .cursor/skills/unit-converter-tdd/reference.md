# UnitConverter TDD — Reference

## C2C 추적 경로

```
PRD-ID → TODO-ID → Test ID → CODE-REF (ECB)
```

문서: `docs/spec/11-traceability-matrix.md`

## ECB 호출 흐름

```
CLI → InputParser.parse(raw) → (unit, value)
CLI → ConvertUseCase.execute(unit, value, registry) → Validator → Converter
```

**금지:** control → boundary import, ConvertUseCase → InputParser

## CODE-REF

| Test ID | ECB | CODE-REF |
|---------|-----|----------|
| CONV-01~04 | entity | `entity.converter.Converter.convert_all()` |
| VAL-01,03,05 | entity | `entity.validator.Validator.validate()` |
| VAL-02,02b,04 | boundary | `boundary.input_parser.InputParser.parse()` |
| FMT-01~03 | boundary | `boundary.formatter.*.format()` |
| CLI-01~04 | boundary | `boundary.cli.main()` |
| CFG-* | infrastructure | `infrastructure.config_loader.ConfigLoader.load()` |
| REG-* | infrastructure, control | `infrastructure.unit_registrar`, `control.register_unit_use_case` |
| UseCase | control | `control.convert_use_case.ConvertUseCase.execute(unit, value, registry)` |
| ARCH-01,02 | — | `/review-ecb` (P1) |

## RED 사이클 (P0)

```
Cycle 1   entity:     CONV-01~04, VAL-01,03,05     tests/entity/
Cycle 1b  boundary:   VAL-02,02b,04                 test_input_parser.py
Cycle 1c  control:    ConvertUseCase                tests/control/
Cycle 2   UI:         FMT-01, CLI-02~04             tests/boundary/
```

## TODO-ID (RED)

| TODO | Test ID |
|------|---------|
| TODO-001 | CONV-01~03 |
| TODO-004 | CONV-04 |
| TODO-005 | VAL-01,05 |
| TODO-006 | VAL-02,02b,04 |
| TODO-007 | VAL-03 |
| TODO-019 | CLI-02~04 |
| TODO-013 | CLI-01 (green) |

## 변환 Golden Values

| 입력 | meter | feet | yard |
|------|-------|------|------|
| meter:2.5 | 2.5 | 8.2 | 2.7 |
| cubit:1 | 0.5 | 1.5 | 0.5 |

문서: `docs/spec/06-conversion-rules.md` §4

## 금지 패턴

| # | 패턴 |
|---|------|
| 1 | converter 단위별 if/elif |
| 2 | feet↔yard 직접 상수 |
| 3 | entity → boundary/control/infrastructure import |
| 4 | control → boundary import |
| 5 | ConvertUseCase가 raw string 파싱 |

## Report / Prompting

Command: `/export-session`
