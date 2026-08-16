---
id: ai-coding-openclaw-oci-review
title: AI 코딩 엔지니어링·OpenClaw·OCI 자동화 검토
status: researched
classification: isolated_research
adopted_by_v2: false
implementation_approved: false
auto_resume: false
created: 2026-08-14
base_commit: e03662f1380370511a9fd1237450765677f3e380
---

# AI 코딩 엔지니어링·OpenClaw·OCI 자동화 검토

> [!warning] 아이디어·조사 기록
> 이 문서는 V2의 공식 결정, 마일스톤 또는 구현 지시가 아니다. Core, Run, 얇은 UI와 자동 연결하지 않으며 별도 사용자 승인 전에는 설치·실험·구현하지 않는다.

## 요약 판정

- 현재 V2의 주된 방식은 **Spec 기반 + Artifact 중심 + 상태·Gate + 사용자 승인 + 독립 검증**이다.
- OpenClaw 전체 도입은 V2의 Orchestrator·도구 실행·기억 기능과 중복되고 권한 면적을 넓힌다. 판정은 **일부 개념만 참고**다.
- OCI 무료 VM에서 사용자가 내보낸 카카오톡 대화 파일을 정리하는 것은 가능하지만, PC 로그인만으로 개인 대화 전체를 서버가 읽는 공식 경로는 확인되지 않았다.
- UI 계약을 바꿀 필수 신규 도구는 없다. 단, 오래된 화면에서 승인하는 사고를 막기 위한 `state_version` 기반 stale-action 차단은 Core/UI 계약의 최소 보완 후보다.

## 1. 현재 V2 엔지니어링 방식

| 방식 | 판정 | 실제 의미 |
|---|---|---|
| 프롬프트 엔지니어링 | 부분 적용 | Skill 호출과 구조화된 작업 지시에 사용 |
| 컨텍스트 엔지니어링 | 적용·검증됨 | Wiki, Run, 승인 Artifact, Commit을 필요한 범위로 전달 |
| Spec 기반 개발 | 적용·검증됨 | Spec Kit의 Specify·Plan·Tasks와 승인 Gate 사용 |
| 루프 엔지니어링 | 부분 적용 | Feature·Change 사이클은 반복했으나 범용 자율 반복 엔진은 아님 |
| Eval 기반 개발 | 적용·검증됨 | Build·Browser·Artifact·사용자 결과를 분리해 판정. 범용 Eval 플랫폼은 없음 |
| 그래프·상태 전이 | 적용·검증됨 | Run stage, status, Gate, pause/resume/차단 상태 사용 |
| 멀티에이전트 | 부분 적용 | Codex·Antigravity 역할 분리는 있으나 별도 Multi-Agent 엔진은 없음 |
| Artifact 중심 | 적용·검증됨 | Spec·Plan·Tasks·Preview·검증 파일의 실재를 성공 조건으로 사용 |
| Gate 기반 | 적용·검증됨 | 승인 전 다음 단계 차단 및 실패 시 정지 |
| Human-in-the-loop | 적용·검증됨 | 디자인·기능 결과의 사용자 판정을 기술 PASS와 분리 |

초보자용 설명: **말로 요청하면 V2가 문서와 실제 결과를 단계별로 만들고, 검증된 것만 다음 단계로 넘기며 중요한 선택은 사용자에게 묻는 방식**이다.

### 강점과 병목

- 강점: 작업 근거 추적, 실패 격리, 승인 전 차단, Commit·Rollback, 기술 검증과 사용자 판정 분리.
- 병목: 내부 정보가 Run·Artifact·Wiki에 나뉘어 있어 초보자가 현재 상태와 다음 행동을 한눈에 보기 어렵다.
- 가장 필요한 보완: 새 프레임워크가 아니라 Core가 `현재 상태 + 근거 + 다음 행동 하나`를 안정적으로 투영하는 것.
- 안전 보완 후보: `ui-state`에 `state_version`, `generated_at`, `source_run_id`를 포함하고 `ui-action`이 같은 `state_version`을 돌려주게 한다. 상태가 바뀌었으면 Core가 오래된 승인·수정 요청을 거부한다.

## 2. OpenClaw

### 확인된 사실

- 공식 대상: `openclaw/openclaw`, OpenClaw Foundation, MIT License.
- 로컬 Gateway가 세션·도구·이벤트·채널의 제어면 역할을 하며 UI·CLI가 연결된다.
- 메시징 채널, 지속 기억, Browser·파일·Shell·Script·Skill 실행을 제공하는 개인용 AI Assistant 성격이다.
- Linux를 지원한다. Oracle Cloud와 Raspberry Pi 호스팅 문서가 있어 ARM 환경 운용 가능성은 높지만, OCI A1에서 사용할 모든 네이티브 의존성은 실제 격리 시험 전까지 확정하지 않는다.
- 광범위한 파일·Shell·외부 채널 권한을 가질 수 있어 비밀키·개인정보·원격 명령의 공격 면적이 크다.

### V2 적합성

- 판정: **일부 개념만 참고**.
- 참고 가치: Gateway와 표시 UI 분리, 휴대폰 메시지 채널, 원격 승인·상태 알림, 선택적 Sandbox.
- 중복: Run, Agent·Tool 실행, Memory, 상태 관리, 중단·재개, Control UI.
- 전체 도입 결과: V2 Core 위에 두 번째 Orchestrator가 생겨 상태 소유권과 복구 책임이 복잡해질 가능성이 높다.
- 얇은 UI 이점: 필수 이점 없음. 모바일 알림·승인 채널은 Core MVP 이후 독립 Adapter 후보로만 검토한다.
- 최소 후속 행동: 재검토 시 V2 저장소·실제 비밀키와 분리한 임시 사용자/컨테이너에서 권한 경계 하나만 시험한다.

## 3. OCI·카카오톡 자동화 주장

### 맞는 부분

- OCI A1은 ARM 기반 Linux 프로그램을 운용할 수 있는 Always Free Compute 후보다.
- 사용자가 카카오톡에서 내보낸 텍스트 파일을 서버나 로컬 프로그램이 분류·요약하는 반자동 처리는 가능하다.
- AI API 또는 ARM에서 실행 가능한 소형 로컬 모델을 분석기에 연결할 수 있다.

### 빠진 부분

- Always Free 인스턴스도 7일 동안 CPU·Network·A1 Memory 사용률이 모두 기준보다 낮으면 유휴 자원으로 회수될 수 있다.
- 홈 리전의 A1 Host Capacity가 부족해 생성이 안 될 수 있으며, 무료 계정은 지원 범위도 제한된다.
- 무료 VM과 AI 모델 비용은 별개다. OpenAI API를 사용하면 ChatGPT 구독과 별도로 API 사용량을 관리해야 한다.
- 공개 서버 운영에는 OS 보안 업데이트, SSH·방화벽·Backup, 비밀키·개인정보 관리 책임이 따른다.
- 내보낸 텍스트와 이미지·첨부 파일은 별도 취급이 필요할 수 있다.

### 과장되거나 확인되지 않은 부분

- PC 카카오톡에 로그인했다는 사실만으로 OCI 서버가 개인 대화 전체를 공식 API로 읽을 수 있다는 근거는 확인되지 않았다.
- Kakao Developers의 공개 KakaoTalk Message API는 메시지 전송 중심이며 개인 채팅 기록 전체 조회 API는 공식 목록에서 확인되지 않았다.
- 화면 자동화로 클라이언트를 조작하는 방법은 깨지기 쉽고 계정·약관·보안 위험이 있어 기본 경로로 추천하지 않는다.
- ‘무료이므로 계속 무중단 운영’은 보장되지 않는다.

### 안전한 최소 방식

```text
사용자가 대화 내보내기
→ 필요한 구간만 선택·민감정보 확인
→ 로컬 또는 격리된 입력 폴더
→ 명시적으로 승인한 모델로 분류·요약
→ Markdown 결과 저장
→ 임시 원문·첨부 처리 정책에 따라 삭제 또는 보관
```

V2 관련성은 현재 Core나 얇은 UI가 아니라 **MVP 이후 사용자 제공 자료 Source Adapter** 후보다.

## 4. 학습·탐색 자료

| 자료 | 성격 | 지금 가치 | 판정 |
|---|---|---|---|
| GitHub Spec Kit | GitHub 공식 OSS | 이미 사용하는 Specify·Plan·Tasks의 의미 이해 | 1순위 |
| Microsoft AI Agents for Beginners | Microsoft 공식 교육·MIT | Tool use, 신뢰성, Human-in-loop 개념 선별 학습 | 2순위, 코드 실습은 나중 |
| OpenAI Cookbook | OpenAI 공식 예제·MIT | Agent·Eval·Sandbox 사례를 실제 필요 시 참고 | 3순위 |
| GitHub `ai-agents` Topic | 커뮤니티 탐색 목록 | 후보 발견만 가능, 검증·안전 보증 없음 | 현재 제외 |
| Prompt Engineering Guide | DAIR.AI 커뮤니티 자료 | 폭넓지만 현재 V2보다 범위가 넓고 초보자에게 과부하 가능 | 필요 시 참고 |

추천 순서 최대 3개:

1. Spec Kit 공식 문서에서 Specify → Plan → Tasks 흐름만 복습
2. Microsoft 과정에서 Agent 개요·Tool Use·Trustworthy Agent만 선택
3. 실제 API 또는 Eval 구현 시 OpenAI Cookbook의 해당 예제만 확인

## 5. 얇은 UI 영향

| 아이디어 | UI 전에 필수 | UI 시안에 반영 | MVP 이후 후보 | 제외 |
|---|---:|---:|---:|---:|
| stale action 차단용 `state_version` 계약 | 후보 1건 | 상태 변경 안내 |  |  |
| 현재 상태를 쉬운 문장으로 표시 |  | 예 |  |  |
| 실제 사용 도구 표시 |  | 예 |  |  |
| 다음 행동 하나만 표시 |  | 예 |  |  |
| OpenClaw 전체 도입 |  |  |  | 예 |
| OpenClaw 모바일 알림·승인 개념 |  |  | 예 |  |
| OCI·카카오톡 Source Adapter |  |  | 예 |  |
| 학습 사이트 UI 메뉴 |  |  |  | 예 |

UI 시안의 기존 5개 계약은 유지한다. 이 조사 때문에 UI 착수를 막을 새 Gate나 새 도구는 만들지 않는다.

## 공식 참고 출처

- [OpenClaw 공식 사이트](https://openclaw.ai/)
- [OpenClaw 공식 GitHub](https://github.com/openclaw/openclaw)
- [OpenClaw 공식 문서](https://docs.openclaw.ai/)
- [Oracle Cloud Always Free Resources](https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm)
- [KakaoTalk Message REST API](https://developers.kakao.com/docs/en/kakaotalk-message/rest-api)
- [Kakao Developers REST API 목록](https://developers.kakao.com/docs/en/rest-api/reference)
- [OpenAI API usage](https://platform.openai.com/docs/api-reference/usage)
- [GitHub Spec Kit](https://github.com/github/spec-kit)
- [Microsoft AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)
- [OpenAI Cookbook](https://github.com/openai/openai-cookbook)
- [Prompt Engineering Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)

## 재개 조건

- OpenClaw: 사용자가 모바일 원격 승인 Adapter 또는 격리 권한 실험을 명시적으로 요청할 때.
- OCI·카카오톡: 실제 내보내기 샘플의 개인정보 처리 범위와 실행 장소를 먼저 승인했을 때.
- 얇은 UI: 사용자가 UI 시안 작업을 재개하라고 할 때 기존 계약과 `state_version` 보완 여부만 확인한다.

## 원본 자료

- 조사 지시서: `/home/user/.codex/attachments/c383e1f9-b9ea-4589-8716-e7ea6457f4a5/pasted-text.txt`
- 조사일: 2026-08-14
