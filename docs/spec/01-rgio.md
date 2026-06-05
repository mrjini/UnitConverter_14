# 01 — R-G-I-O 설계 (STEP 2)

## 주제 (한 문장)

**길이 단위 변환 CLI의 요구·검증·구현을 PRD → To-Do → Test ID → Code로 일대일 추적 가능하게 설계하고, Mom Test에서 드러난 "수동 재검증 비용"을 자동화된 테스트와 단일 변환 기준(meter 경유)으로 제거한다.**

---

## R-G-I-O 표

| 구분 | 정의 | UnitConverter_14 내용 |
|------|------|------------------------|
| **R — Reality (현재)** | 지금 있는 상태와 진짜 문제 | 단일 스크립트(`UnitConverter.py`)에 변환·검증·출력이 혼재. 변환 비율이 코드 상수로 박혀 있고, feet↔yard를 meter 경유 없이 따로 두면 불일치 위험. 검증 기준이 README·메모·손계산에 흩어져, 상수·입력 규칙 변경 시마다 **처음부터 다시 맞춰 보는** 비용 발생. |
| **G — Goal (목표)** | 달성하려는 상태 | PRD·시나리오·Test ID·코드가 **추적 가능한** Dual-Track TDD 구조. meter를 **유일 기준(base unit)**으로 두고 변환·검증·출력을 **역할 분리(SRP)** 하며, 단위·포맷·설정 확장 시 **기존 코드 수정 최소(OCP)**. RED→GREEN→REFACTOR 사이클마다 "맞는지"를 **테스트 ID로 즉시 확인**. |
| **I — Input (입력·전제·제약)** | 설계·구현의 재료와 경계 | **도메인:** `unit:value`, meter/feet/yard, `1m=3.28084ft=1.09361yd`, feet↔yard는 meter 경유. **품질:** OCP, SRP, 음수·형식·미등록 단위 검증. **확장:** units.json/YAML, cubit 동적 등록, `--format json\|csv\|table`. **프로세스:** C2C, Dual-Track TDD, ARRR. **브랜치:** main→staging→spec→red→green→refactoring→new_features. **SPEC 제약:** 구현 코드·RED 테스트 작성 금지. |
| **O — Output (산출물)** | 단계별 결과물 | **SPEC:** PRD, R-G-I-O, 용어집, 기능·I/O·검증·변환·설정·설계 명세, 시나리오 카탈로그, Dual-Track 계획, 추적 매트릭스, 품질 체크리스트. **RED:** pytest 실패 테스트. **GREEN:** 최소 통과 구현. **REFACTOR:** OCP/SRP 정렬. **new_features:** 설정·cubit·포맷 확장. |

---

## 성공 기준 (5개)

| # | 기준 | 측정 방법 |
|---|------|-----------|
| **SC-1 추적성** | PRD 요구 1건당 To-Do, Test ID, Code Ref가 양방향 연결 | 추적 매트릭스 orphan **0건** |
| **SC-2 변환 정확성** | 모든 변환이 meter 경유 단일 공식, README 비율 일치 | CONV-* 테스트 전부 통과; feet↔yard 직접 상수 금지 |
| **SC-3 검증 자동화** | 음수·형식·미등록 단위를 Test ID로 재현·회귀 검증 | VAL-* 리팩터 후에도 동일 Test ID 유지·통과 |
| **SC-4 확장 비용** | cubit·설정·포맷 추가 시 Converter 핵심 수정 없음 | new_features OCP 체크리스트 충족; 기존 테스트 회귀 없음 |
| **SC-5 재검증 시간** | 상수·규칙 변경 시 pytest 1회로 Go/No-Go | 수동 엑셀·검색 비교 불필요 |

---

## 하지 않을 것

| 구분 | 내용 |
|------|------|
| SPEC | 구현 코드·pytest/RED 테스트 작성 |
| 설계 | feet↔yard 직접 비율 상수 도입 |
| 범위 | GUI, 웹 API, 다중 물리량(질량·온도) |
| 품질 | SRP/OCP 사후 정당화 |
| 프로세스 | Test ID·PRD ID 없이 코드·테스트 작성 |
| 출력 | 반올림 규칙 미명세 상태로 구현 |
| 확장 | SPEC에서 cubit·json·설정 파일 실구현 |

---

## Mom Test 연결

| Mom Test | R-G-I-O 반영 |
|----------|--------------|
| 표면 문제 | O — CLI + 형식 검증 + 출력 포맷 산출물 |
| 진짜 문제 | G — meter 경유 + Test ID 추적으로 재검증 비용 제거 |
| 40분 상수 불일치 | SC-2, CONV-04 (meter 경유 강제) |
| 1시간 수동 비교표 재작업 | SC-3, SC-5, Dual-Track TDD |
