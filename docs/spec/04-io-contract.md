# 04 — I/O Contract (입·출력 계약)

## 1. 입력 (Input)

### 1.1 변환 입력 (stdin)

| 필드 | 규칙 |
|------|------|
| **형식** | `{unit}:{value}` |
| **unit** | 등록된 단위명, 공백 없음, 대소문자 구분 |
| **value** | 10진수 부동소수 (`float` 파싱 가능), `0` 이상 |
| **구분자** | 첫 번째 `:` 만 unit/value 구분 (value에 `:` 없음 가정) |

**유효 예:**
```
meter:2.5
feet:0
yard:100
cubit:1        # P2 — 등록 후
```

**무효 예:**

| 입력 | 오류 |
|------|------|
| `meter2.5` | ERR_FORMAT |
| `:2.5` | ERR_FORMAT |
| `meter:` | ERR_FORMAT |
| `meter:abc` | ERR_NUMBER |
| `meter:-1` | ERR_NEGATIVE |
| `mile:1` | ERR_UNKNOWN_UNIT |

### 1.2 CLI 옵션 (P2)

| 옵션 | 타입 | 기본값 | 설명 |
|------|------|--------|------|
| `--format` | enum | `table` | `table`, `json`, `csv` |
| `--config` | path | (내장 기본값) | units 설정 파일 |
| `--register` | string | — | `1 {unit} = {ratio} meter` |

### 1.3 동적 등록 표현 (P2)

```
1 {unit_name} = {positive_number} meter
```

예: `1 cubit = 0.4572 meter`

---

## 2. 출력 (Output)

### 2.1 공통 필드

모든 포맷은 다음 논리 레코드를 표현한다.

| 필드 | 타입 | 설명 |
|------|------|------|
| `input_unit` | string | 사용자 입력 단위 |
| `input_value` | number | 사용자 입력 값 (원본) |
| `target_unit` | string | 변환 대상 단위 |
| `target_value` | number | 변환 결과 (1자리 반올림) |

### 2.2 table (기본, P0)

한 줄 per 변환. 입력 단위 포함 **모든 등록 단위** 출력.

```
{input_value} {input_unit} = {target_value} {target_unit}
```

- `target_value`: 소수점 1자리 (예: `8.2`, `2.7`)
- 단위 순서: Registry 등록 순 (기본: meter → feet → yard)

**예 — `meter:2.5`:**
```
2.5 meter = 2.5 meter
2.5 meter = 8.2 feet
2.5 meter = 2.7 yard
```

### 2.3 json (P2)

stdout에 JSON 배열. 오류 시 stderr + non-zero exit.

```json
[
  {
    "input_unit": "meter",
    "input_value": 2.5,
    "target_unit": "feet",
    "target_value": 8.2
  },
  {
    "input_unit": "meter",
    "input_value": 2.5,
    "target_unit": "yard",
    "target_value": 2.7
  }
]
```

- `input_value`: 원본 float
- `target_value`: 반올림 후 float (1자리)

### 2.4 csv (P2)

```csv
input_unit,input_value,target_unit,target_value
meter,2.5,meter,2.5
meter,2.5,feet,8.2
meter,2.5,yard,2.7
```

- UTF-8, LF 줄바꿈
- 헤더 행 필수

---

## 3. 오류 출력 (stderr)

| 코드 | 메시지 템플릿 | Exit |
|------|---------------|:----:|
| ERR_FORMAT | `Invalid format. Use unit:value (ex: meter:2.5)` | 1 |
| ERR_NUMBER | `Invalid number: {value_str}` | 1 |
| ERR_NEGATIVE | `Negative value not allowed: {value}` | 1 |
| ERR_UNKNOWN_UNIT | `Unknown unit: {unit}` | 1 |
| ERR_CONFIG | `Config error: {detail}` | 2 |
| ERR_REGISTRATION | `Registration error: {detail}` | 2 |

메시지는 [05-validation-spec.md](./05-validation-spec.md)와 일치해야 한다.

---

## 4. 반올림 규칙

| 항목 | 규칙 |
|------|------|
| 방법 | Round half up (Python `round(x, 1)`) |
| 자릿수 | 1 |
| 적용 시점 | **출력 직전** (내부 계산은 full precision) |

**검증 앵커:** `meter:2.5` → feet `8.2`, yard `2.7` (README 예시)
