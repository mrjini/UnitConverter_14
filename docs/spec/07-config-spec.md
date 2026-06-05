# 07 — Config Spec (설정 외부화 명세)

## 1. 목적

변환 비율을 코드 상수에서 분리하여 **설정 파일**로 로드한다. (PRD-013)

---

## 2. 지원 형식

| 형식 | 확장자 | 우선순위 |
|------|--------|----------|
| JSON | `.json` | 1 (기본) |
| YAML | `.yaml`, `.yml` | 2 (선택) |

`--config` 미지정 시 **내장 기본 Registry** (meter, feet, yard) 사용.

---

## 3. JSON 스키마

### 3.1 구조

```json
{
  "base_unit": "meter",
  "units": {
    "meter": 1.0,
    "feet": 0.3048,
    "yard": 0.9144
  }
}
```

| 필드 | 타입 | 필수 | 설명 |
|------|------|:----:|------|
| `base_unit` | string | ✓ | `"meter"` 고정 |
| `units` | object | ✓ | unit_name → to_meter_factor |

**to_meter_factor:** `1 {unit} = factor meter`

### 3.2 기본 units.json (예시 — GREEN에서 생성)

```json
{
  "base_unit": "meter",
  "units": {
    "meter": 1.0,
    "feet": 0.304799735,
    "yard": 0.914401828
  }
}
```

> factor = 1 / README 비율 (feet: 1/3.28084, yard: 1/1.09361)

### 3.3 YAML 동등 예시

```yaml
base_unit: meter
units:
  meter: 1.0
  feet: 0.304799735
  yard: 0.914401828
```

---

## 4. 검증 규칙 (로드 시)

| 규칙 | 오류 |
|------|------|
| 파일 없음 | ERR_CONFIG |
| JSON/YAML 파싱 실패 | ERR_CONFIG |
| `base_unit` ≠ `meter` | ERR_CONFIG |
| `units` 비어 있음 | ERR_CONFIG |
| factor ≤ 0 | ERR_CONFIG |
| `meter` factor ≠ 1.0 | ERR_CONFIG |
| 중복 unit명 (object key) | (JSON parser 처리) |

**Test ID:** CFG-01 (정상 로드), CFG-02 (오류)

---

## 5. ConfigLoader 책임 (infrastructure)

| 메서드 | 설명 |
|--------|------|
| `load(path: str) -> UnitRegistry` | 파일 파싱 → Registry 구성 |
| `load_default() -> UnitRegistry` | 내장 기본 3단위 |

**ECB:** infrastructure — control/CLI가 호출해 Registry를 **구성**; entity는 완성된 Registry만 사용.

**CODE-REF:** `infrastructure.config_loader.ConfigLoader`

---

## 6. 동적 등록과의 관계

1. ConfigLoader(infrastructure)로 Registry 초기화 — control/CLI 경유
2. `--register` → UnitRegistrar(infrastructure) + RegisterUnitUseCase(control)
3. ConvertUseCase(control) → entity.Converter

**Test ID:** REG-01 (cubit 등록 후 변환)

---

## 7. OCP

- 새 단위: JSON에 key 추가만 (Converter 수정 없음)
- 새 파일 형식: ConfigLoader에 Loader 구현 추가 (Registry/Converter 불변)

---

## 8. SPEC 단계 제외

- `units.json` 실 파일 생성 → GREEN/new_features
- PyYAML 설치 → GREEN 단계 requirements 결정
