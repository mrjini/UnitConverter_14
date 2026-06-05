# SPEC 문서 가이드

UnitConverter_14 **spec** 브랜치 산출물. 구현 코드·RED 테스트는 **작성하지 않음**.

## 읽는 순서

| 순서 | 문서 | 목적 |
|:----:|------|------|
| 1 | [00-glossary.md](./00-glossary.md) | 용어 |
| 2 | [01-rgio.md](./01-rgio.md) | R-G-I-O, 성공 기준 |
| 3 | [02-prd.md](./02-prd.md) | 요구사항 |
| 4 | [03-functional-spec.md](./03-functional-spec.md) | 기능·흐름 |
| 5 | [04-io-contract.md](./04-io-contract.md) | 입·출력 |
| 6 | [05-validation-spec.md](./05-validation-spec.md) | 검증 규칙 |
| 7 | [06-conversion-rules.md](./06-conversion-rules.md) | 변환 공식 |
| 8 | [08-design-spec.md](./08-design-spec.md) | OCP/SRP |
| 9 | [09-scenario-catalog.md](./09-scenario-catalog.md) | Test ID 시나리오 |
| 10 | [10-dual-track-plan.md](./10-dual-track-plan.md) | TDD 순서 |
| 11 | [11-traceability-matrix.md](./11-traceability-matrix.md) | PRD↔Test↔Code |
| 12 | [07-config-spec.md](./07-config-spec.md) | 설정 (P2) |
| 13 | [12-quality-checklist.md](./12-quality-checklist.md) | merge 게이트 |

## 프로세스 문서

- [../process/c2c-workflow.md](../process/c2c-workflow.md)
- [../process/mom-test-summary.md](../process/mom-test-summary.md)

## 브랜치 전략

```
main → staging → spec → red → green → refactoring → new_features
                      ↑ 현재
```

## spec → red 착수 조건

1. [12-quality-checklist.md](./12-quality-checklist.md) SPEC 게이트 통과
2. P0 시나리오(09) 확정
3. `spec` → `staging` PR (선택) → `red` 브랜치 생성

## ARRR

| 단계 | 브랜치 |
|------|--------|
| Ask | red |
| Respond | green |
| Refine | refactoring |
| Repeat | spec 갱신 → red |
