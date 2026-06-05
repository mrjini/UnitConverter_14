# C2C Workflow (Cursor to Code)

## 1. 개요

UnitConverter_14는 **C2C** + **Dual-Track TDD** + **ARRR** 로 개발한다.

| 약어 | 의미 |
|------|------|
| C2C | Cursor(AI) ↔ Code 협업, 명세 기반 프롬프트 |
| ARRR | Ask=RED, Respond=GREEN, Refine=REFACTOR, Repeat=문서→RED |

---

## 2. 브랜치 전략

```
main
 └── staging          # 통합·릴리스 후보
      └── spec        # 명세 (구현·RED 테스트 없음)
           └── red    # 실패 테스트 (Ask)
                └── green        # 최소 구현 (Respond)
                     └── refactoring  # SRP/OCP (Refine)
                          └── new_features  # P2 확장 (Repeat)
```

### Merge 방향

- `new_features` → `refactoring` → `green` → `red` → `spec` → `staging` → `main`
- 각 단계: [12-quality-checklist.md](../spec/12-quality-checklist.md) 게이트

---

## 3. C2C 추적 경로

```
PRD-ID  ──1:N──▶  TODO-ID  ──1:1──▶  TEST-ID  ──1:N──▶  CODE-REF
```

상세: [11-traceability-matrix.md](../spec/11-traceability-matrix.md)

---

## 4. ARRR 사이클

### Ask (RED)

**목표:** 실패하는 테스트만 추가.

**AI 프롬프트 템플릿:**
```
브랜치: red
Test ID: {CONV|VAL|FMT}-xx
참조: docs/spec/09-scenario-catalog.md 해당 섹션
작업: pytest 실패 테스트만 작성. 구현 코드 수정 금지.
Given-When-Then 준수. Test ID를 test name/docstring에 포함.
```

**금지:** GREEN 구현, REFACTOR

---

### Respond (GREEN)

**목표:** Test ID 통과하는 **최소** 코드.

**AI 프롬프트 템플릿:**
```
브랜치: green
Test ID: {목록}
참조: docs/spec/08-design-spec.md ECB CODE-REF ({layer}.{module})
작업: RED 테스트를 green으로. 해당 ECB 레이어에만 최소 구현.
```

**금지:** SRP 분리(REFACTOR), P2 기능

---

### Refine (REFACTORING)

**목표:** OCP/SRP 정렬, 테스트 green 유지.

**AI 프롬프트 템플릿:**
```
브랜치: refactoring
참조: docs/spec/08-design-spec.md ECB, 12-quality-checklist
작업: boundary→control→entity 의존 정렬, Formatter Protocol.
모든 P0 Test ID green 유지.
```

---

### Repeat (문서 → RED)

**목표:** P2 요구 SPEC 갱신 후 다음 RED.

1. `spec` 브랜치에서 PRD/시나리오 갱신
2. `new_features`에서 RED Cycle 3~5
3. ARRR 반복

---

## 5. Dual-Track + ECB

| Track | ECB | Harness | RED 순서 |
|-------|-----|---------|----------|
| A | entity, control | `tests/entity/`, `tests/control/` | CONV → VAL → UseCase |
| B | boundary, infrastructure | `tests/boundary/` | FMT → CLI → CFG → REG |

문서: [10-dual-track-plan.md](../spec/10-dual-track-plan.md), [08-design-spec.md](../spec/08-design-spec.md)

**CODE-REF 프롬프트 예:** `entity.converter.Converter.convert_all()`

---

## 6. SPEC 단계 규칙

| 허용 | 금지 |
|------|------|
| docs/spec/*, docs/process/* | `src/unit_converter/` 구현 (Harness 제외) |
| ECB Harness (`__init__.py`) | pytest 작성 |
| PRD, 시나리오, 설계 | units.json 생성 |

---

## 7. RED 착수 체크리스트

- [ ] spec 문서 00~12 완료
- [ ] P0 Test ID 목록 확정
- [ ] `git checkout -b red` (from spec)
- [ ] TODO-001~009 순서대로 RED

---

## 8. AI 협업 팁 (Activities 회고용)

- **항상 Test ID + spec 경로**를 프롬프트에 포함
- RED/GREEN **브랜치 명시**로 scope creep 방지
- Mom Test 진짜 문제 → CONV-04, VAL-* 우선
