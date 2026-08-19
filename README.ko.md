<picture><source media="(prefers-color-scheme: dark)" srcset="docs/hero-dark.svg"><img src="docs/hero-light.svg" width="900" alt="profile-cover"></picture>

**GitHub 프로필 README를 잡지 페이지처럼 디자인하는 에이전트
스킬.** 위 마스트헤드가 곧 제품입니다. 동봉 스크립트가 Fraunces를
커닝까지 살려 SVG 패스로 변환하므로 외부 리소스가 전혀 없고, 어떤
OS에서든 동일하게 렌더되며, 깨진 이미지가 뜰 일이 없습니다.

[English](README.md)

## 위젯 대신 타이포그래피

대부분의 프로필 README는 서드파티 통계 카드와 뱃지 더미입니다.
레이트리밋에 걸리고, 503을 띄우고, 다 비슷하게 생겼습니다.
profile-cover는 그 자리를 타이포그래피로 바꿉니다. 링크여야 하는
것들은 전부 순수 마크다운으로 남아서 클릭되고 검색됩니다.

아키타입 3종이 함께 옵니다. shipping ledger(자주 출시하는 사람),
build log(공부 기록), stewardship(하나를 오래 지키는 메인테이너).
영문 README에 보이는 스트립들은 스크린샷이 아니라 GitHub이 지금
렌더하고 있는 실제 SVG입니다.

## 설치

```sh
npx skills add sjh9714/profile-cover
pip install fonttools uharfbuzz
```

설치 후 한마디면 됩니다.

> 내 GitHub 프로필 README 디자인해줘.

에이전트가 인터뷰하고, 아키타입을 고르고, 동봉 스크립트로 마스트헤드를
생성하고, GitHub 네이티브 README를 조립한 뒤 결정적 검사기를 통과시켜
전달합니다.

## 검사기가 강제하는 것

- 악센트는 라이트/다크 페어, 둘 다 4.5:1 대비 통과
- SVG에 외부 리소스 금지, 마크다운에 inline style 금지(GitHub이 제거),
  빈 표 헤더 금지
- 12.5px 미만 라벨 금지 (모바일 가독 하한)
- 부패하는 카피("이번 주", 실시간 수치)와 서드파티 동적 이미지는 경고

## 형제 프로젝트

[repo-cover](https://github.com/sjh9714/repo-cover)는 같은 디자인
언어로 레포의 소셜 프리뷰 카드를 만듭니다.

## 라이선스

MIT. Fraunces 폰트는 SIL OFL로 동봉 (`skills/profile-cover/assets/OFL.txt`).
