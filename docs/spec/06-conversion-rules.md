# 06 — Conversion Rules (변환 규칙 명세)

## 1. 기준

| 항목 | 값 |
|------|-----|
| **Base unit** | `meter` |
| **1 meter** | `3.28084 feet` |
| **1 meter** | `1.09361 yard` |

---

## 2. Registry 표현

각 단위는 **base unit(meter) 대비 비율**로 저장한다.

```
unit_name → meters_per_unit   # 1 unit = N meters
```

| Unit | meters_per_unit | 계산 |
|------|-----------------|------|
| meter | 1.0 | 기준 |
| feet | 1 / 3.28084 ≈ 0.3048 | 1 feet = 0.3048 m |
| yard | 1 / 1.09361 ≈ 0.9144 | 1 yard = 0.9144 m |

**저장 방식 (택1, GREEN에서 결정):**

- **A:** `to_meter_factor` — 1 unit = factor meter (위 표)
- **B:** `from_meter_factor` — 1 meter = factor unit (README 비율)

내부 일관성만 유지하면 됨. SPEC 권장: **A (to_meter_factor)** — 변환 공식 단순화.

---

## 3. 변환 공식 (meter 경유)

### 3.1 입력 → base (meter)

```
meter_value = input_value × registry[input_unit].to_meter_factor
```

- meter 입력: `meter_value = input_value`

### 3.2 base → 대상 단위

```
target_value_raw = meter_value / registry[target_unit].to_meter_factor
target_value_display = round(target_value_raw, 1)
```

### 3.3 금지 패턴

```
# ❌ 금지 — feet ↔ yard 직접 상수
FEET_TO_YARD = ...
yard_value = feet_value * FEET_TO_YARD
```

```
# ✅ 필수 — meter 경유
meter_value = feet_value * (1/3.28084)
yard_value = meter_value / (1/1.09361)
```

**Test ID:** CONV-04

---

## 4. 검증 앵커 (Golden Values)

| 입력 | 대상 | raw (full) | display (1자리) |
|------|------|------------|-----------------|
| meter:2.5 | meter | 2.5 | 2.5 |
| meter:2.5 | feet | 8.2021 | **8.2** |
| meter:2.5 | yard | 2.734025 | **2.7** |
| feet:8.2 | meter | ≈2.499... | **2.5** |
| yard:2.7 | meter | ≈2.469... | **2.5** (역변환 시 README 예시와 ±0.1 허용) |

**CONV-01~03:** meter/feet/yard 입력 시 모든 단위 출력  
**CONV-04:** feet→yard 결과가 meter 경유와 동일 (직접 상수 사용 시 실패)

---

## 5. cubit (P2)

등록: `1 cubit = 0.4572 meter`

```
cubit.to_meter_factor = 0.4572
```

`cubit:1` → meter = 0.4572, feet/yard는 §3 공식 적용.

**Test ID:** REG-01, CONV-05

---

## 6. 정밀도 정책

| 단계 | 정밀도 |
|------|--------|
| 내부 계산 | IEEE 754 double, full precision |
| 출력 | round half up, 1자리 |
| 테스트 assert | display 값 비교 (1자리) |

---

## 7. Mom Test 연결

| 문제 | 규칙 |
|------|------|
| feet/yard 각각 상수 → 40분 불일치 | §3 meter 경유 필수, CONV-04 |
| README 8.2/2.7 불일치 | §4 Golden Values, §6 반올림 |
