# 00 — Glossary (용어집)

> UnitConverter_14 SPEC 문서에서 사용하는 용어 정의.

## 도메인 용어

| 용어 | 정의 |
|------|------|
| **Length Unit (길이 단위)** | 길이를 표현하는 명명 단위. 초기 지원: `meter`, `feet`, `yard`. |
| **Base Unit (기준 단위)** | 모든 변환의 중간 기준. 본 프로젝트에서 **`meter`** 가 유일한 base unit. |
| **Unit Registry (단위 등록부)** | 등록된 단위 이름과 base unit 대비 비율을 보관·조회하는 컴포넌트. |
| **Conversion Ratio (변환 비율)** | `1 base_unit = N target_unit` 형태의 상수. feet/yard 간 직접 비율은 사용하지 않음. |
| **unit:value** | CLI 입력 형식. 콜론(`:`)으로 단위명과 수치를 구분. 예: `meter:2.5`. |
| **Dynamic Registration (동적 등록)** | 런타임에 `1 cubit = 0.4572 meter` 형태로 새 단위를 등록하는 기능. |
| **Output Format (출력 포맷)** | 변환 결과 표현 방식. `table`(기본), `json`, `csv`. |

## 변환 규칙 용어

| 용어 | 정의 |
|------|------|
| **Meter 경유 변환** | 임의 단위 A→B 변환 시 `A → meter → B` 2단계로 계산. |
| **Direct Ratio (직접 비율)** | 두 비-base 단위 간 상수. **본 프로젝트에서 금지.** |
| **Display Precision (표시 정밀도)** | 출력 시 소수점 자릿수. 기본 **1자리**, 반올림(round half up). |

## 아키텍처 용어

| 용어 | 정의 |
|------|------|
| **SRP (Single Responsibility Principle)** | 클래스/모듈은 변경 이유가 하나만 존재. |
| **OCP (Open-Closed Principle)** | 확장(새 단위·포맷)에는 열려 있고, 기존 변환 로직 수정에는 닫혀 있음. |
| **Dual-Track TDD** | Track A(도메인) + Track B(통합/CLI)로 테스트를 분리하는 TDD 전략. |

## 프로세스 용어

| 용어 | 정의 |
|------|------|
| **C2C** | Cursor to Code. AI 협업 기반 개발 워크플로. |
| **ARRR** | Ask=RED, Respond=GREEN, Refine=REFACTOR, Repeat=문서 갱신 후 다음 RED. |
| **PRD-ID** | 제품 요구 식별자. `PRD-xxx`. |
| **Test ID** | 시나리오·테스트 식별자. `CONV-*`, `VAL-*`, `FMT-*`, `CFG-*`, `REG-*`, `CLI-*`. |
| **TODO-ID** | 작업 항목 식별자. `TODO-xxx`. |
| **CODE-REF** | 구현 대상 모듈/클래스/함수 참조. SPEC 단계에서는 이름만 정의. |

## 오류 분류

| 코드 | 의미 |
|------|------|
| **ERR_FORMAT** | `unit:value` 형식 위반 (콜론 없음, 빈 단위/값 등). |
| **ERR_NUMBER** | 값 파싱 실패 (숫자가 아님). |
| **ERR_NEGATIVE** | 음수 값. |
| **ERR_UNKNOWN_UNIT** | 등록되지 않은 단위. |
| **ERR_CONFIG** | 설정 파일 로드·파싱 실패. |
| **ERR_REGISTRATION** | 동적 등록 문법·비율 오류. |
