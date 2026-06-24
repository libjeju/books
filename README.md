# 제주대학교 중앙도서관 추천도서 아카이브 운영 매뉴얼

이 저장소는 제주대학교 중앙도서관의 추천도서 콘텐츠를 GitHub Pages로 공개하기 위한 공간입니다.

- 뉴스레터
- 카드뉴스
- 이메일 발송용 본문
- 포스터 다운로드 자료
- 회차별 추천도서 아카이브

를 한곳에서 관리합니다.

이 매뉴얼은 GitHub를 처음 사용하는 사람도 그대로 따라 할 수 있도록 작성했습니다.

---

## 1. 가장 중요한 원칙

### 1-1. 기존 HTML은 수정하지 않습니다

이미 제작된 뉴스레터와 카드뉴스 HTML은 원본 콘텐츠입니다.

다음 항목은 임의로 바꾸지 않습니다.

- 뉴스레터 HTML의 디자인
- 뉴스레터 HTML의 문구
- 카드뉴스 HTML의 디자인
- 카드뉴스 HTML의 문구
- 도서 표지 이미지
- 카드뉴스 이미지
- 기존 CSS와 이미지 경로

새 회차를 추가할 때는 기존 파일을 수정하는 것이 아니라, **새 회차 폴더를 만들어 그 안에 새 자료를 추가**합니다.

### 1-2. 회차별로 독립 보관합니다

이 저장소는 1년에 6차례, 격월 단위로 추천도서 콘텐츠를 계속 추가하기 위한 구조입니다.

예시:

```text
issues/2026-01/  ← 2026년 1번째 추천도서
issues/2026-02/  ← 2026년 2번째 추천도서
issues/2026-03/  ← 2026년 3번째 추천도서
issues/2026-04/  ← 2026년 4번째 추천도서, 현재 회차
issues/2026-05/  ← 2026년 5번째 추천도서
issues/2026-06/  ← 2026년 6번째 추천도서
```

여기서 `2026-04`는 2026년 4월이라는 뜻이 아니라, **2026년 4번째 추천도서 회차**라는 뜻으로 사용합니다.

### 1-3. 파일명과 폴더명은 영어, 숫자, 하이픈을 권장합니다

웹주소가 깨지지 않도록 파일명에는 가능하면 한글, 공백, 괄호를 쓰지 않습니다.

권장:

```text
poster-a4.pdf
poster-web.jpg
book-01.jpg
2026-04
```

비권장:

```text
추천도서 포스터 최종.pdf
카드뉴스(수정본).png
도서 표지 1.jpg
```

---

## 2. 이 저장소의 전체 구조

현재 권장 구조는 아래와 같습니다.

```text
books
├─ index.html
├─ 404.html
├─ README.md
├─ .nojekyll
└─ issues
   └─ 2026-04
      ├─ index.html
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
      ├─ posters
      │  ├─ index.html
      │  ├─ README.md
      │  ├─ print
      │  ├─ web
      │  └─ source
      └─ tools
```

---

## 3. 공개 주소

GitHub 계정이 `libjeju`이고 리포지터리 이름이 `books`이면 기본 주소는 아래와 같습니다.

```text
https://libjeju.github.io/books/
```

현재 회차 주소는 아래와 같습니다.

```text
전체 추천도서 아카이브 홈
https://libjeju.github.io/books/

2026년 4번째 추천도서 회차 홈
https://libjeju.github.io/books/issues/2026-04/

뉴스레터
https://libjeju.github.io/books/issues/2026-04/newsletter/2026-07-08/

카드뉴스
https://libjeju.github.io/books/issues/2026-04/cardnews/2026-07-08/

이메일 발송용 페이지
https://libjeju.github.io/books/issues/2026-04/email/2026-07-08/

포스터 다운로드 페이지
https://libjeju.github.io/books/issues/2026-04/posters/
```

---

## 4. 처음 GitHub에 올리는 방법

이 부분은 저장소를 처음 만들 때 한 번만 하면 됩니다.

### 4-1. GitHub에 새 리포지터리 만들기

1. 웹브라우저에서 GitHub에 접속합니다.

   ```text
   https://github.com
   ```

2. `libjeju` 계정으로 로그인합니다.

3. 화면 오른쪽 위의 `+` 버튼을 클릭합니다.

4. 메뉴에서 `New repository`를 클릭합니다.

5. `Owner`가 `libjeju`인지 확인합니다.

6. `Repository name`에 아래처럼 입력합니다.

   ```text
   books
   ```

7. `Public`을 선택합니다.

   누구나 볼 수 있게 하려면 반드시 `Public`이어야 합니다.

8. `Add a README file`은 체크하지 않습니다.

9. `Add .gitignore`는 `None` 그대로 둡니다.

10. `Choose a license`는 `None` 그대로 둡니다.

11. 초록색 `Create repository` 버튼을 클릭합니다.

---

### 4-2. 파일 업로드 화면 열기

리포지터리를 만들면 `https://github.com/libjeju/books` 화면으로 이동합니다.

화면에 따라 다음 중 하나를 선택합니다.

#### 경우 A. `uploading an existing file` 문구가 보이는 경우

1. 화면 가운데의 `uploading an existing file` 링크를 클릭합니다.

#### 경우 B. 파일 목록 화면이 보이는 경우

1. 파일 목록 위쪽의 `Add file` 버튼을 클릭합니다.
2. 메뉴에서 `Upload files`를 클릭합니다.

---

### 4-3. 내 컴퓨터의 `bookrecs` 폴더 내용 올리기

중요합니다.

`bookrecs` 폴더 자체를 올리는 것이 아닙니다.

`bookrecs` 폴더 **안에 들어간 뒤**, 그 안의 파일과 폴더를 모두 선택해서 올려야 합니다.

올바른 업로드 결과:

```text
books/index.html
books/README.md
books/issues/2026-04/index.html
books/issues/2026-04/newsletter/...
books/issues/2026-04/cardnews/...
books/issues/2026-04/posters/...
```

잘못된 업로드 결과:

```text
books/bookrecs/index.html
books/bookrecs/issues/2026-04/...
```

잘못된 구조가 되면 웹주소가 달라지고, 이미지나 링크가 깨질 수 있습니다.

#### 업로드 순서

1. Windows 파일 탐색기를 엽니다.

2. 압축을 푼 `bookrecs` 폴더로 이동합니다.

3. `bookrecs` 폴더를 더블클릭해서 안으로 들어갑니다.

4. 안에 다음 파일과 폴더가 보이는지 확인합니다.

   ```text
   index.html
   README.md
   404.html
   .nojekyll
   issues
   ```

5. 키보드에서 `Ctrl + A`를 눌러 모두 선택합니다.

6. 선택된 파일과 폴더를 GitHub의 업로드 화면으로 끌어다 놓습니다.

7. 업로드가 끝날 때까지 기다립니다.

8. 화면 아래의 `Commit changes` 영역으로 내려갑니다.

9. 커밋 메시지에 아래처럼 입력합니다.

   ```text
   추천도서 아카이브 최초 업로드
   ```

10. `Commit directly to the main branch`가 선택되어 있는지 확인합니다.

11. 초록색 `Commit changes` 버튼을 클릭합니다.

---

## 5. GitHub Pages 설정 방법

파일을 올린 뒤에는 GitHub Pages를 켜야 웹사이트 주소가 열립니다.

### 5-1. Pages 설정 화면으로 이동

1. `https://github.com/libjeju/books`로 이동합니다.

2. 저장소 상단 메뉴에서 `Settings`를 클릭합니다.

   상단 메뉴 예시:

   ```text
   Code | Issues | Pull requests | Actions | Projects | Wiki | Security | Insights | Settings
   ```

3. 왼쪽 메뉴에서 `Code and automation` 구역을 찾습니다.

4. 그 아래의 `Pages`를 클릭합니다.

---

### 5-2. 배포 방식 설정

`Build and deployment` 영역에서 아래처럼 설정합니다.

```text
Source: Deploy from a branch
Branch: main
Folder: /(root)
```

순서:

1. `Source` 드롭다운을 클릭합니다.
2. `Deploy from a branch`를 선택합니다.
3. `Branch` 항목에서 첫 번째 드롭다운을 클릭합니다.
4. `main`을 선택합니다.
5. 두 번째 드롭다운에서 `/(root)`를 선택합니다.
6. `Save` 버튼을 클릭합니다.

---

### 5-3. 공개 주소 확인

잠시 기다린 뒤 아래 주소를 엽니다.

```text
https://libjeju.github.io/books/
```

처음에는 바로 안 열릴 수 있습니다. 몇 분 정도 기다린 뒤 다시 새로고침합니다.

---

## 6. 새 추천도서 회차 추가 방법

새 회차를 추가할 때는 기존 회차를 수정하지 말고 새 폴더를 만듭니다.

예를 들어 2026년 5번째 추천도서를 추가한다면 아래 폴더를 만듭니다.

```text
issues/2026-05/
```

그 안에 아래 구조를 만듭니다.

```text
issues/2026-05
├─ index.html
├─ newsletter
├─ cardnews
├─ email
├─ assets
└─ posters
   ├─ index.html
   ├─ README.md
   ├─ print
   ├─ web
   └─ source
```

### 6-1. GitHub 웹사이트에서 새 폴더를 만드는 방법

GitHub는 빈 폴더만 따로 만들 수 없습니다.

폴더를 만들려면 그 폴더 안에 파일을 하나 만들어야 합니다.

예를 들어 `issues/2026-05/posters/print` 폴더를 만들고 싶다면 다음처럼 합니다.

1. GitHub에서 `books` 저장소로 이동합니다.
2. `Add file` 버튼을 클릭합니다.
3. `Create new file`을 클릭합니다.
4. 파일 이름 칸에 아래처럼 입력합니다.

   ```text
   issues/2026-05/posters/print/.gitkeep
   ```

5. 화면 아래 `Commit changes` 버튼을 클릭합니다.

그러면 `issues → 2026-05 → posters → print` 폴더가 생성됩니다.

`.gitkeep`은 빈 폴더를 유지하기 위해 넣는 빈 파일입니다.

### 6-2. 새 회차 자료를 추가하는 기본 순서

1. 새 회차 폴더를 만듭니다.

   예시:

   ```text
   issues/2026-05/
   ```

2. 뉴스레터 자료를 넣습니다.

   예시:

   ```text
   issues/2026-05/newsletter/2026-09-10/index.html
   ```

3. 카드뉴스 자료를 넣습니다.

   예시:

   ```text
   issues/2026-05/cardnews/2026-09-10/index.html
   ```

4. 이메일 발송용 자료를 넣습니다.

   예시:

   ```text
   issues/2026-05/email/2026-09-10/index.html
   ```

5. 도서 표지와 공통 이미지를 넣습니다.

   예시:

   ```text
   issues/2026-05/assets/covers/2026-09-10/
   ```

6. 포스터 자료를 넣습니다.

   예시:

   ```text
   issues/2026-05/posters/print/poster-a4.pdf
   issues/2026-05/posters/web/poster-web.jpg
   issues/2026-05/posters/source/poster-source.pptx
   ```

7. 전체 목록 페이지 `index.html`에 새 회차 링크를 추가합니다.

---

## 7. 포스터 관리 방법

포스터는 회차별 `posters` 폴더에서 관리합니다.

```text
issues/2026-04/posters/
```

포스터 폴더 안은 다음처럼 나눕니다.

```text
posters
├─ print   ← 인쇄용 고해상도 파일
├─ web     ← 웹 게시용 이미지
└─ source  ← 원본 편집파일
```

### 7-1. print 폴더

인쇄용 파일을 넣습니다.

예시:

```text
issues/2026-04/posters/print/poster-a4.pdf
issues/2026-04/posters/print/poster-a3.pdf
issues/2026-04/posters/print/poster-a4.png
```

### 7-2. web 폴더

홈페이지, 게시판, 문자, 카카오톡 공유용 이미지를 넣습니다.

예시:

```text
issues/2026-04/posters/web/poster-web.jpg
issues/2026-04/posters/web/poster-square.png
```

### 7-3. source 폴더

원본 편집 파일을 넣습니다.

예시:

```text
issues/2026-04/posters/source/poster-source.pptx
issues/2026-04/posters/source/poster-source.psd
issues/2026-04/posters/source/poster-source.ai
```

주의:

- 원본 편집 파일에 저작권 문제가 있는 이미지가 포함되어 있다면 공개 저장소에 올리지 않습니다.
- 내부용 자료, 개인정보, 미공개 문서는 올리지 않습니다.
- GitHub Pages로 공개하면 누구나 접근할 수 있습니다.

---

## 8. 포스터 다운로드 주소 만들기

파일을 올리면 주소는 폴더 구조 그대로 만들어집니다.

예를 들어 아래 파일을 올렸다면,

```text
issues/2026-04/posters/print/poster-a4.pdf
```

다운로드 주소는 아래가 됩니다.

```text
https://libjeju.github.io/books/issues/2026-04/posters/print/poster-a4.pdf
```

웹용 포스터 파일이 아래라면,

```text
issues/2026-04/posters/web/poster-web.jpg
```

주소는 아래가 됩니다.

```text
https://libjeju.github.io/books/issues/2026-04/posters/web/poster-web.jpg
```

---

## 9. GitHub에 파일을 추가 업로드하는 방법

새 포스터나 새 이미지를 나중에 추가할 때는 다음 순서로 합니다.

1. GitHub에서 `books` 저장소로 이동합니다.

   ```text
   https://github.com/libjeju/books
   ```

2. 파일을 넣을 폴더로 이동합니다.

   예시:

   ```text
   issues → 2026-04 → posters → print
   ```

3. 오른쪽 위 또는 파일 목록 위쪽의 `Add file` 버튼을 클릭합니다.

4. `Upload files`를 클릭합니다.

5. 내 컴퓨터의 파일을 GitHub 화면으로 끌어다 놓습니다.

6. 화면 아래 `Commit changes` 영역으로 이동합니다.

7. 커밋 메시지를 입력합니다.

   예시:

   ```text
   포스터 인쇄용 파일 추가
   ```

8. `Commit changes` 버튼을 클릭합니다.

9. 몇 분 뒤 GitHub Pages 주소에서 파일이 열리는지 확인합니다.

---

## 10. 전체 목록 페이지에 새 회차 링크 추가하기

새 회차를 추가하면 `index.html`에 링크를 추가해야 합니다.

이 파일은 전체 추천도서 아카이브의 첫 화면입니다.

### 10-1. GitHub에서 index.html 수정하기

1. GitHub에서 `books` 저장소 첫 화면으로 이동합니다.
2. 파일 목록에서 `index.html`을 클릭합니다.
3. 오른쪽 위의 연필 모양 아이콘을 클릭합니다.
4. 기존 회차 카드 아래에 새 회차 링크를 추가합니다.
5. 화면 아래로 내려갑니다.
6. 커밋 메시지를 입력합니다.

   예시:

   ```text
   2026년 5번째 추천도서 링크 추가
   ```

7. `Commit changes` 버튼을 클릭합니다.

주의:

- `newsletter`와 `cardnews` 원본 HTML을 수정하는 것이 아닙니다.
- 전체 목록 페이지인 `index.html`에 링크만 추가합니다.

---

## 11. 이메일 발송 전 확인사항

학교 구성원에게 전체 발송하기 전에 본인에게 먼저 시험 발송합니다.

확인할 것:

- 뉴스레터 링크가 열리는가
- 카드뉴스 링크가 열리는가
- 포스터 다운로드 링크가 열리는가
- 스마트폰에서 화면이 잘 보이는가
- 이미지가 빠지지 않았는가
- 주소가 `https://libjeju.github.io/books/`로 시작하는가

---

## 12. 자주 생기는 문제와 해결법

### 문제 1. 404 Not Found가 뜹니다

확인할 것:

```text
Settings → Pages
Source: Deploy from a branch
Branch: main
Folder: /(root)
```

또한 `index.html`이 저장소 맨 위에 있어야 합니다.

올바른 위치:

```text
books/index.html
```

잘못된 위치:

```text
books/bookrecs/index.html
```

### 문제 2. 이미지만 안 보입니다

확인할 것:

- 이미지 파일을 GitHub에 올렸는가
- HTML에 적힌 파일명과 실제 파일명이 같은가
- 대문자와 소문자가 일치하는가
- 폴더 위치가 맞는가

예를 들어 아래 두 파일명은 서로 다릅니다.

```text
poster-web.jpg
Poster-Web.jpg
```

### 문제 3. 새 폴더가 안 만들어집니다

GitHub는 빈 폴더만 따로 만들 수 없습니다.

폴더 안에 `.gitkeep` 같은 빈 파일을 하나 만들어야 합니다.

예시:

```text
issues/2026-05/posters/web/.gitkeep
```

### 문제 4. 주소에 `/books/`가 빠졌습니다

`books` 저장소를 쓰면 주소에는 반드시 `/books/`가 들어갑니다.

올바른 주소:

```text
https://libjeju.github.io/books/
```

잘못된 주소:

```text
https://libjeju.github.io/
```

---

## 13. 공개 저장소에 올리면 안 되는 것

이 저장소가 `Public`이면 누구나 볼 수 있습니다.

다음 자료는 올리지 않습니다.

- 개인정보가 포함된 파일
- 내부 결재문서
- 비공개 업무자료
- 저작권 문제가 있는 원본 편집파일
- 외부 공개 권한이 없는 이미지
- 학교 내부에서만 사용해야 하는 자료

---

## 14. 운영 체크리스트

처음 업로드할 때:

```text
□ books 리포지터리를 Public으로 만들었다
□ bookrecs 폴더 안의 내용물을 업로드했다
□ bookrecs 폴더 자체를 올리지 않았다
□ index.html이 저장소 최상위에 있다
□ issues/2026-04 폴더가 있다
□ GitHub Pages를 main / root로 설정했다
□ https://libjeju.github.io/books/ 주소가 열린다
```

새 회차를 추가할 때:

```text
□ 새 회차 폴더를 만들었다
□ 기존 회차 폴더를 수정하거나 덮어쓰지 않았다
□ 뉴스레터 HTML을 새 회차 폴더에 넣었다
□ 카드뉴스 HTML을 새 회차 폴더에 넣었다
□ 이미지 폴더를 함께 넣었다
□ 포스터 파일을 posters 폴더에 넣었다
□ 전체 index.html에 새 회차 링크를 추가했다
□ PC와 스마트폰에서 링크를 확인했다
```

---

## 15. 현재 회차 관리 메모

현재 회차:

```text
2026년 4번째 추천도서
폴더명: issues/2026-04
주제: 달을 읽는 여름밤
```

현재 회차 주요 주소:

```text
회차 홈
https://libjeju.github.io/books/issues/2026-04/

뉴스레터
https://libjeju.github.io/books/issues/2026-04/newsletter/2026-07-08/

카드뉴스
https://libjeju.github.io/books/issues/2026-04/cardnews/2026-07-08/

이메일 발송용 페이지
https://libjeju.github.io/books/issues/2026-04/email/2026-07-08/

포스터 다운로드 페이지
https://libjeju.github.io/books/issues/2026-04/posters/
```

---

## 16. 참고 공식 문서

- GitHub 저장소 만들기와 파일 업로드  
  https://docs.github.com/en/get-started/start-your-journey/uploading-a-project-to-github

- GitHub Pages 시작하기  
  https://docs.github.com/pages/quickstart

- GitHub Pages 게시 소스 설정  
  https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
