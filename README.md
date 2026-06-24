# 제주대학교 중앙도서관 추천도서 아카이브 운영 매뉴얼

이 저장소는 제주대학교 중앙도서관 추천도서 콘텐츠를 격월 단위로 누적 관리하기 위한 GitHub Pages 저장소입니다.

뉴스레터, 카드뉴스, 이메일 발송용 페이지, 포스터 자료를 회차별로 보관하고, 누구나 웹주소로 접속할 수 있도록 운영합니다.

---

## 1. 기본 정보

### GitHub 저장소

```text
https://github.com/libjeju/books
```

### 공개 웹사이트 주소

```text
https://libjeju.github.io/books/
```

### 현재 등록된 회차

```text
2026년 4번째 추천도서
폴더명: issues/2026-04
```

---

## 2. 현재 회차 주요 주소

### 전체 추천도서 아카이브 홈

```text
https://libjeju.github.io/books/
```

### 2026년 4번째 추천도서 회차 홈

```text
https://libjeju.github.io/books/issues/2026-04/
```

### 뉴스레터

```text
https://libjeju.github.io/books/issues/2026-04/newsletter/2026-07-08/
```

### 카드뉴스

```text
https://libjeju.github.io/books/issues/2026-04/cardnews/2026-07-08/
```

### 이메일 발송용 페이지

```text
https://libjeju.github.io/books/issues/2026-04/email/2026-07-08/
```

### 포스터 자료 페이지

```text
https://libjeju.github.io/books/issues/2026-04/posters/
```

---

## 3. 운영 원칙

이 저장소는 추천도서 콘텐츠를 장기적으로 누적 관리하기 위한 공간입니다.

가장 중요한 원칙은 다음과 같습니다.

```text
1. 기존 뉴스레터 HTML은 수정하지 않는다.
2. 기존 카드뉴스 HTML은 수정하지 않는다.
3. 기존 회차 폴더는 삭제하지 않는다.
4. 새 추천도서는 새 회차 폴더에 추가한다.
5. 이미지 파일 이름과 위치를 함부로 바꾸지 않는다.
6. GitHub Pages 주소가 깨지지 않도록 기존 경로를 유지한다.
7. 공개 저장소이므로 개인정보, 내부자료, 저작권 문제가 있는 파일은 올리지 않는다.
```

---

## 4. 전체 폴더 구조

현재 저장소의 기본 구조는 다음과 같습니다.

```text
books
├─ index.html
├─ README.md
├─ 404.html
├─ .nojekyll
└─ issues
   └─ 2026-04
      ├─ index.html
      ├─ README.md
      ├─ newsletter
      │  └─ 2026-07-08
      │     └─ index.html
      ├─ cardnews
      │  └─ 2026-07-08
      │     ├─ index.html
      │     └─ png
      ├─ email
      │  └─ 2026-07-08
      │     └─ index.html
      ├─ assets
      │  └─ covers
      │     └─ 2026-07-08
      ├─ posters
      └─ tools
```

---

## 5. 폴더별 역할

### `index.html`

전체 추천도서 아카이브 첫 화면입니다.

주소는 다음과 같습니다.

```text
https://libjeju.github.io/books/
```

새 회차를 추가하면 이 파일에 새 회차 링크를 추가할 수 있습니다.

---

### `issues`

추천도서 회차별 자료가 들어가는 폴더입니다.

예시:

```text
issues/2026-04
issues/2026-05
issues/2026-06
```

---

### `issues/2026-04`

2026년 4번째 추천도서 자료가 들어 있는 회차 폴더입니다.

이 폴더 안에는 뉴스레터, 카드뉴스, 이메일 발송용 페이지, 포스터 자료가 함께 들어 있습니다.

---

### `newsletter`

뉴스레터 HTML이 들어가는 폴더입니다.

예시:

```text
issues/2026-04/newsletter/2026-07-08/
```

주의:

```text
뉴스레터 HTML의 디자인과 문구는 임의로 수정하지 않습니다.
```

---

### `cardnews`

카드뉴스 HTML과 PNG 이미지가 들어가는 폴더입니다.

예시:

```text
issues/2026-04/cardnews/2026-07-08/
```

주의:

```text
카드뉴스 HTML의 디자인과 문구는 임의로 수정하지 않습니다.
```

---

### `email`

이메일 발송용 본문 복사 페이지가 들어가는 폴더입니다.

예시:

```text
issues/2026-04/email/2026-07-08/
```

이 페이지는 학교 구성원에게 뉴스레터를 발송할 때 사용할 수 있습니다.

---

### `assets`

도서 표지, 이미지, CSS, 기타 웹 자원이 들어가는 폴더입니다.

예시:

```text
issues/2026-04/assets/covers/2026-07-08/
```

주의:

```text
이미지 파일 이름을 바꾸면 뉴스레터나 카드뉴스에서 이미지가 깨질 수 있습니다.
```

---

### `posters`

포스터 자료를 보관하는 폴더입니다.

예시:

```text
issues/2026-04/posters/
```

포스터는 필요에 따라 관리자가 다운로드해서 사용할 수 있도록 보관합니다.

권장 구조는 다음과 같습니다.

```text
posters
├─ print
├─ web
└─ source
```

각 폴더의 역할은 다음과 같습니다.

```text
print  : 인쇄용 고해상도 포스터 PDF, PNG
web    : 홈페이지, 게시판, SNS용 가벼운 이미지
source : 원본 편집파일
```

주의:

```text
source 폴더에는 저작권 문제나 내부자료가 포함된 원본 파일을 올리지 않도록 주의합니다.
```

---

## 6. 처음 GitHub에 업로드할 때의 원칙

컴퓨터에서 압축을 푼 폴더명이 `bookrecs`라면, GitHub에는 `bookrecs` 폴더 자체를 올리는 것이 아닙니다.

반드시 `bookrecs` 폴더 안으로 들어간 뒤, 그 안의 파일과 폴더를 모두 선택해서 올립니다.

올바른 구조:

```text
books
├─ index.html
├─ README.md
├─ 404.html
└─ issues
```

잘못된 구조:

```text
books
└─ bookrecs
   ├─ index.html
   ├─ README.md
   └─ issues
```

잘못된 구조가 되면 웹주소가 꼬이거나 페이지가 열리지 않을 수 있습니다.

---

## 7. GitHub에서 파일을 업로드하는 방법

### 1단계. 저장소 접속

아래 주소로 접속합니다.

```text
https://github.com/libjeju/books
```

---

### 2단계. 파일 업로드 화면 열기

저장소 화면에서 다음 순서로 클릭합니다.

```text
Add file → Upload files
```

---

### 3단계. 내 컴퓨터에서 파일 선택

컴퓨터에서 업로드할 폴더 안으로 들어갑니다.

예시:

```text
bookrecs 폴더 더블클릭
```

그 안에서 전체 선택합니다.

```text
Ctrl + A
```

---

### 4단계. GitHub 화면으로 드래그

선택된 파일과 폴더를 GitHub 업로드 화면으로 끌어다 놓습니다.

GitHub 화면에는 다음과 비슷한 문구가 보입니다.

```text
Drag files here to add them to your repository
```

---

### 5단계. Commit changes 클릭

업로드가 끝나면 화면 아래쪽에서 커밋 메시지를 입력합니다.

예시:

```text
추천도서 자료 업로드
```

그 다음 아래 버튼을 클릭합니다.

```text
Commit changes
```

---

## 8. GitHub Pages 설정 방법

GitHub Pages는 GitHub 저장소에 올린 HTML 파일을 웹사이트로 공개하는 기능입니다.

처음 한 번만 설정하면 됩니다.

### 1단계. Settings 클릭

저장소 상단 메뉴에서 다음을 클릭합니다.

```text
Settings
```

---

### 2단계. Pages 클릭

왼쪽 메뉴에서 다음 항목을 찾습니다.

```text
Code and automation → Pages
```

---

### 3단계. Build and deployment 설정

아래처럼 설정합니다.

```text
Source: Deploy from a branch
Branch: main
Folder: /(root)
```

---

### 4단계. Save 클릭

설정을 마친 뒤 다음 버튼을 클릭합니다.

```text
Save
```

---

### 5단계. 공개 주소 확인

몇 분 후 아래 주소가 열리는지 확인합니다.

```text
https://libjeju.github.io/books/
```

---

## 9. 새 추천도서 회차를 추가하는 방법

추천도서는 1년에 6차례, 격월 단위로 추가합니다.

새 회차를 추가할 때는 기존 회차를 수정하지 않고 새 폴더를 만듭니다.

예를 들어 2026년 5번째 추천도서를 추가한다면 다음 폴더를 만듭니다.

```text
issues/2026-05
```

권장 구조는 다음과 같습니다.

```text
issues/2026-05
├─ index.html
├─ README.md
├─ newsletter
├─ cardnews
├─ email
├─ assets
└─ posters
```

---

## 10. 새 회차를 추가할 때의 순서

### 1단계. 새 회차 폴더 준비

컴퓨터에서 새 회차 폴더를 만듭니다.

예시:

```text
2026-05
```

---

### 2단계. 새 회차 자료를 넣기

새 회차 폴더 안에 다음 자료를 넣습니다.

```text
newsletter
cardnews
email
assets
posters
index.html
README.md
```

---

### 3단계. GitHub에 업로드

GitHub 저장소에서 다음을 클릭합니다.

```text
Add file → Upload files
```

업로드할 때는 새 회차 폴더가 다음 위치에 들어가도록 해야 합니다.

```text
issues/2026-05
```

---

### 4단계. 전체 아카이브 홈에 링크 추가

새 회차를 추가한 뒤에는 전체 홈인 `index.html`에도 새 회차 링크를 추가하는 것이 좋습니다.

수정할 파일:

```text
index.html
```

예시 링크:

```html
<a href="./issues/2026-05/">2026년 5번째 추천도서 보기</a>
```

---

### 5단계. 새 주소 확인

예상 주소는 다음과 같습니다.

```text
https://libjeju.github.io/books/issues/2026-05/
```

뉴스레터와 카드뉴스 주소는 실제 폴더명에 따라 달라집니다.

예시:

```text
https://libjeju.github.io/books/issues/2026-05/newsletter/2026-09-10/
https://libjeju.github.io/books/issues/2026-05/cardnews/2026-09-10/
```

---

## 11. 포스터 자료 추가 방법

포스터 파일은 해당 회차의 `posters` 폴더에 넣습니다.

예시:

```text
issues/2026-04/posters/
```

권장 파일 위치는 다음과 같습니다.

### 인쇄용 포스터

```text
issues/2026-04/posters/print/
```

예시 파일명:

```text
poster-a4.pdf
poster-a3.pdf
poster-print.png
```

---

### 웹 게시용 포스터

```text
issues/2026-04/posters/web/
```

예시 파일명:

```text
poster-web.jpg
poster-square.png
```

---

### 원본 편집파일

```text
issues/2026-04/posters/source/
```

예시 파일명:

```text
poster-source.pptx
poster-source.psd
poster-source.ai
```

주의:

```text
원본 편집파일에 저작권 문제, 유료 폰트, 내부자료, 개인정보가 포함되어 있으면 공개 저장소에 올리지 않습니다.
```

---

## 12. 포스터 다운로드 주소 예시

포스터 파일을 아래 위치에 올렸다고 가정합니다.

```text
issues/2026-04/posters/web/poster-web.jpg
```

그러면 공개 주소는 다음과 같습니다.

```text
https://libjeju.github.io/books/issues/2026-04/posters/web/poster-web.jpg
```

인쇄용 PDF를 아래 위치에 올렸다면,

```text
issues/2026-04/posters/print/poster-a4.pdf
```

공개 주소는 다음과 같습니다.

```text
https://libjeju.github.io/books/issues/2026-04/posters/print/poster-a4.pdf
```

---

## 13. 이메일 발송 전 확인할 것

학교 구성원에게 이메일을 전체 발송하기 전에 반드시 본인에게 먼저 테스트 메일을 보냅니다.

확인할 내용은 다음과 같습니다.

```text
1. 뉴스레터 링크가 열리는가
2. 카드뉴스 링크가 열리는가
3. 이미지가 정상적으로 보이는가
4. 스마트폰에서 화면이 깨지지 않는가
5. 학교 메일에서 링크가 차단되지 않는가
6. 버튼이나 링크를 클릭했을 때 올바른 페이지로 이동하는가
```

---

## 14. 이메일에 넣기 좋은 링크

이메일 본문에는 최소한 다음 링크를 넣습니다.

### 뉴스레터 보기

```text
https://libjeju.github.io/books/issues/2026-04/newsletter/2026-07-08/
```

### 카드뉴스 보기

```text
https://libjeju.github.io/books/issues/2026-04/cardnews/2026-07-08/
```

### 전체 아카이브 보기

```text
https://libjeju.github.io/books/
```

---

## 15. 스마트폰 확인 방법

반드시 스마트폰에서도 확인합니다.

권장 확인 방법은 다음과 같습니다.

```text
1. 스마트폰에서 Wi-Fi를 끈다.
2. LTE 또는 5G 상태로 접속한다.
3. 뉴스레터 주소를 연다.
4. 카드뉴스 주소를 연다.
5. 이미지가 잘 보이는지 확인한다.
6. 글자가 너무 작지 않은지 확인한다.
7. 버튼과 링크가 정상 작동하는지 확인한다.
```

Wi-Fi를 끄고 확인하는 이유는 실제 외부 접속 환경에서도 잘 보이는지 확인하기 위해서입니다.

---

## 16. 링크와 이미지가 깨지지 않게 하는 규칙

### 파일명 규칙

가능하면 파일명은 영어 소문자, 숫자, 하이픈을 사용합니다.

권장:

```text
poster-web.jpg
book-01.png
card-01.png
```

비권장:

```text
추천 도서 포스터 최종.jpg
카드뉴스 1번.png
```

---

### 경로 규칙

웹에서는 역슬래시 `\`가 아니라 슬래시 `/`를 사용합니다.

권장:

```html
<img src="./assets/covers/2026-07-08/cosmos.png">
```

비권장:

```html
<img src=".\assets\covers\2026-07-08\cosmos.png">
```

---

### 컴퓨터 내부 경로 사용 금지

HTML 안에 내 컴퓨터 경로가 들어가면 다른 사람에게는 이미지가 보이지 않습니다.

비권장:

```html
<img src="D:\bookrecs\image.png">
```

비권장:

```html
<img src="file:///D:/bookrecs/image.png">
```

권장:

```html
<img src="./assets/covers/2026-07-08/cosmos.png">
```

---

## 17. 404 오류가 날 때 확인할 것

페이지에 접속했는데 `404`가 나오면 다음을 확인합니다.

```text
1. GitHub Pages 설정이 되어 있는가
2. Branch가 main인가
3. Folder가 /(root)인가
4. index.html 파일이 해당 폴더에 있는가
5. 주소의 철자가 정확한가
6. 대소문자가 일치하는가
7. 업로드 후 몇 분 기다렸는가
```

예를 들어 다음 주소가 열리려면,

```text
https://libjeju.github.io/books/issues/2026-04/
```

아래 파일이 있어야 합니다.

```text
issues/2026-04/index.html
```

---

## 18. 이미지가 보이지 않을 때 확인할 것

이미지가 보이지 않으면 다음을 확인합니다.

```text
1. 이미지 파일이 GitHub에 올라가 있는가
2. 이미지 파일명이 HTML에 적힌 이름과 같은가
3. 대소문자가 같은가
4. 이미지 폴더 위치가 바뀌지 않았는가
5. 파일 확장자가 .jpg인지 .png인지 정확한가
6. HTML 안에 D:\ 같은 내 컴퓨터 경로가 들어가 있지 않은가
```

예를 들어 HTML에 아래처럼 적혀 있다면,

```html
<img src="./assets/covers/2026-07-08/cosmos.png">
```

실제 파일도 아래 위치에 있어야 합니다.

```text
assets/covers/2026-07-08/cosmos.png
```

---

## 19. GitHub에서 빈 폴더가 안 보일 때

GitHub는 빈 폴더를 저장하지 않습니다.

예를 들어 아래 폴더가 비어 있으면 GitHub에 보이지 않을 수 있습니다.

```text
posters/print
posters/web
posters/source
```

이것은 오류가 아닙니다.

빈 폴더를 유지하려면 그 안에 `README.md` 같은 안내 파일을 하나 넣으면 됩니다.

---

## 20. 공개 저장소에 올리면 안 되는 자료

이 저장소는 Public 저장소입니다.

따라서 누구나 볼 수 있습니다.

다음 자료는 올리지 않습니다.

```text
1. 개인정보가 포함된 파일
2. 내부 결재문서
3. 비공개 회의자료
4. 저작권 문제가 있는 원본 이미지
5. 유료 폰트 파일
6. 외부 공개가 허용되지 않은 도서 표지 원본
7. 계정 비밀번호나 API 키
8. 계약서, 견적서 등 민감한 행정자료
```

---

## 21. 새 회차 추가 전 체크리스트

새 추천도서 회차를 추가하기 전에 다음을 확인합니다.

```text
□ 새 회차 폴더명을 정했다. 예: 2026-05
□ 기존 회차 폴더를 덮어쓰지 않는다.
□ 뉴스레터 HTML이 준비되어 있다.
□ 카드뉴스 HTML이 준비되어 있다.
□ 도서 표지 이미지가 모두 있다.
□ 카드뉴스 PNG 이미지가 모두 있다.
□ 포스터 자료가 있다면 posters 폴더에 넣는다.
□ index.html 파일이 회차 폴더 안에 있다.
□ 공개하면 안 되는 파일이 없는지 확인했다.
```

---

## 22. 업로드 후 체크리스트

업로드 후 다음을 확인합니다.

```text
□ GitHub에 새 회차 폴더가 보인다.
□ 새 회차 index.html이 있다.
□ 뉴스레터 주소가 열린다.
□ 카드뉴스 주소가 열린다.
□ 이메일 발송용 페이지가 열린다.
□ 포스터 자료 페이지가 열린다.
□ 이미지가 누락되지 않는다.
□ 스마트폰에서도 정상 표시된다.
□ 전체 아카이브 홈에서 새 회차로 이동할 수 있다.
```

---

## 23. 현재 회차 운영 완료 체크리스트

2026년 4번째 추천도서는 다음 항목이 정상 작동하면 운영 준비가 완료된 것입니다.

```text
□ 전체 아카이브 홈 접속 가능
□ 2026년 4번째 추천도서 회차 홈 접속 가능
□ 뉴스레터 페이지 접속 가능
□ 카드뉴스 페이지 접속 가능
□ 이메일 발송용 페이지 접속 가능
□ 포스터 자료 페이지 접속 가능
□ PC에서 정상 표시
□ 스마트폰에서 정상 표시
□ 다른 사람 PC에서도 정상 접속 가능
□ 이메일 테스트 발송 완료
```

---

## 24. 관리자가 꼭 기억할 것

```text
기존 자료는 고치지 말고, 새 자료는 새 폴더에 추가한다.
```

```text
뉴스레터와 카드뉴스 HTML은 최종본으로 보존한다.
```

```text
파일명과 폴더 위치를 바꾸면 이미지와 링크가 깨질 수 있다.
```

```text
전체 발송 전에는 반드시 본인에게 테스트 메일을 보낸다.
```

```text
스마트폰에서는 Wi-Fi를 끄고 LTE 또는 5G로도 확인한다.
```

---

## 25. 빠른 작업 순서 요약

### 기존 회차 확인

```text
1. https://libjeju.github.io/books/ 접속
2. 회차 홈 접속
3. 뉴스레터 접속
4. 카드뉴스 접속
5. 이메일 발송용 페이지 접속
6. 스마트폰 확인
```

### 새 회차 추가

```text
1. 새 회차 폴더 생성
2. newsletter 폴더 추가
3. cardnews 폴더 추가
4. email 폴더 추가
5. assets 폴더 추가
6. posters 폴더 추가
7. GitHub에 업로드
8. 전체 index.html에 새 회차 링크 추가
9. GitHub Pages 주소 확인
10. 이메일 테스트 발송
```

---

## 26. 문의 또는 수정이 필요한 경우

다음과 같은 경우에는 작업 전에 구조를 먼저 확인합니다.

```text
1. 뉴스레터 디자인을 바꾸고 싶은 경우
2. 카드뉴스 파일명을 바꾸고 싶은 경우
3. 이미지 폴더를 옮기고 싶은 경우
4. 새 회차 주소 체계를 바꾸고 싶은 경우
5. 포스터 원본파일을 공개해도 되는지 애매한 경우
6. 기존 회차를 삭제하거나 수정해야 하는 경우
```

가능하면 기존 회차는 그대로 보존하고, 새 회차를 추가하는 방식으로 운영합니다.

---

# 끝

이 저장소는 제주대학교 중앙도서관 추천도서 콘텐츠를 장기적으로 축적하기 위한 공개 아카이브입니다.

운영의 핵심은 다음 세 가지입니다.

```text
1. 회차별로 독립 보관한다.
2. 기존 HTML은 수정하지 않는다.
3. 새 자료는 새 폴더에 추가한다.
```
