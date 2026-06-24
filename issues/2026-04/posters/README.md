# 2026년 4회차 추천도서 포스터 자료

이 폴더는 **2026년 4회차 추천도서 포스터 자료**를 보관하는 곳입니다.

포스터는 용도별로 나누어 관리합니다.

```text
posters
├─ web
├─ print
└─ source
```

---

## 1. 이 폴더의 목적

이 폴더는 추천도서 홍보용 포스터를 보관하고, 필요한 관리자가 언제든지 다운로드해서 사용할 수 있도록 하기 위한 공간입니다.

포스터는 다음 용도로 사용할 수 있습니다.

```text
도서관 홈페이지 게시
학교 홈페이지 게시
도서관 게시판 게시
카카오톡, 문자, SNS 홍보
인쇄 게시
QR코드 연결
추후 수정 및 재활용
```

---

## 2. 포스터 폴더 구조

### `web`

웹 게시용 포스터를 넣습니다.

사용 예:

```text
홈페이지 게시
게시판 첨부
SNS 게시
카카오톡 공유
문자 링크 공유
QR코드 연결
```

권장 파일 형식:

```text
jpg
png
webp
```

권장 파일명:

```text
poster-2026-04-web-main.jpg
poster-2026-04-web-square.png
poster-2026-04-web-story.png
```

---

### `print`

인쇄용 포스터를 넣습니다.

사용 예:

```text
A4 출력
A3 출력
도서관 게시판 부착
행사용 출력물
```

권장 파일 형식:

```text
pdf
png
jpg
```

권장 파일명:

```text
poster-2026-04-print-a4.pdf
poster-2026-04-print-a3.pdf
poster-2026-04-print-a4.png
```

---

### `source`

원본 편집파일을 넣습니다.

사용 예:

```text
문구 수정
날짜 수정
다음 회차 디자인 재활용
인쇄용 재편집
```

권장 파일 형식:

```text
pptx
ai
psd
fig
indd
```

권장 파일명:

```text
poster-2026-04-source.pptx
poster-2026-04-source.ai
poster-2026-04-source.psd
```

주의:

```text
source 폴더에는 외부 공개가 가능한 파일만 올립니다.
유료 폰트 파일, 내부자료, 개인정보, 저작권 문제가 있는 원본 이미지는 올리지 않습니다.
```

---

## 3. 파일명 규칙

포스터 파일명은 다음 규칙을 사용합니다.

```text
poster-회차-용도-세부구분.확장자
```

현재 회차는 `2026-04`입니다.

따라서 파일명은 다음과 같이 작성합니다.

```text
poster-2026-04-web-main.jpg
poster-2026-04-web-square.png
poster-2026-04-print-a4.pdf
poster-2026-04-print-a3.pdf
poster-2026-04-source.pptx
```

---

## 4. 파일명 작성 원칙

파일명에는 다음만 사용합니다.

```text
영어 소문자
숫자
하이픈 -
확장자
```

좋은 예:

```text
poster-2026-04-web-main.jpg
poster-2026-04-print-a4.pdf
poster-2026-04-source.pptx
```

피해야 할 예:

```text
최종 포스터.jpg
추천도서 포스터 7-8월.png
poster final.jpg
포스터_최종_수정본.pdf
2026년 4회차 포스터.png
```

피해야 하는 이유:

```text
한글 파일명은 일부 시스템에서 주소가 길고 복잡해질 수 있습니다.
공백은 링크 오류의 원인이 될 수 있습니다.
최종, 최종2, 진짜최종 같은 이름은 나중에 관리하기 어렵습니다.
```

---

## 5. 포스터 업로드 방법

### 1단계. GitHub 저장소 접속

아래 주소로 접속합니다.

```text
https://github.com/libjeju/books
```

---

### 2단계. 포스터 폴더로 이동

다음 순서대로 클릭합니다.

```text
issues
→ 2026-04
→ posters
```

현재 위치가 아래처럼 보여야 합니다.

```text
books / issues / 2026-04 / posters
```

---

### 3단계. 용도에 맞는 폴더로 이동

웹 게시용이면:

```text
web
```

인쇄용이면:

```text
print
```

원본 편집파일이면:

```text
source
```

---

### 4단계. 파일 업로드

해당 폴더 안에서 다음 순서로 클릭합니다.

```text
Add file
→ Upload files
```

그 다음 컴퓨터에서 파일을 끌어다 놓습니다.

업로드가 끝나면 아래쪽에 커밋 메시지를 입력합니다.

예:

```text
2026년 4회차 웹 게시용 포스터 추가
```

마지막으로 다음 버튼을 클릭합니다.

```text
Commit changes
```

---

## 6. web, print, source 폴더가 보이지 않을 때

GitHub는 빈 폴더를 표시하지 않을 수 있습니다.

따라서 `web`, `print`, `source` 폴더가 보이지 않으면 아래 방법을 사용합니다.

### 방법 1. 컴퓨터에서 폴더를 만들어 업로드

컴퓨터에서 아래 구조를 만듭니다.

```text
poster-upload
├─ web
│  └─ poster-2026-04-web-main.jpg
├─ print
│  └─ poster-2026-04-print-a4.pdf
└─ source
   └─ poster-2026-04-source.pptx
```

그 다음 GitHub의 `posters` 폴더 화면에서 다음 순서로 진행합니다.

```text
Add file
→ Upload files
→ web, print, source 폴더를 드래그
→ Commit changes
```

이렇게 하면 GitHub에 폴더가 자동으로 만들어집니다.

---

### 방법 2. GitHub에서 새 파일로 폴더 만들기

GitHub에서 폴더만 따로 만들 수는 없습니다.

대신 폴더 안에 파일을 하나 만들면 폴더가 생깁니다.

예를 들어 `web` 폴더를 만들려면:

```text
Add file
→ Create new file
```

파일 이름 칸에 아래처럼 입력합니다.

```text
web/README.md
```

본문에 간단히 적습니다.

```text
웹 게시용 포스터 보관 폴더입니다.
```

그 다음:

```text
Commit changes
```

이렇게 하면 `web` 폴더가 만들어집니다.

---

## 7. 포스터 공개 주소

포스터를 GitHub에 올리면 GitHub Pages 주소로 접근할 수 있습니다.

### 웹 게시용 포스터 주소 예시

파일 위치:

```text
issues/2026-04/posters/web/poster-2026-04-web-main.jpg
```

공개 주소:

```text
https://libjeju.github.io/books/issues/2026-04/posters/web/poster-2026-04-web-main.jpg
```

---

### 인쇄용 PDF 주소 예시

파일 위치:

```text
issues/2026-04/posters/print/poster-2026-04-print-a4.pdf
```

공개 주소:

```text
https://libjeju.github.io/books/issues/2026-04/posters/print/poster-2026-04-print-a4.pdf
```

---

### 원본 편집파일 주소 예시

파일 위치:

```text
issues/2026-04/posters/source/poster-2026-04-source.pptx
```

공개 주소:

```text
https://libjeju.github.io/books/issues/2026-04/posters/source/poster-2026-04-source.pptx
```

주의:

```text
source 폴더의 파일도 공개 주소를 알면 누구나 다운로드할 수 있습니다.
따라서 공개해도 되는 원본만 업로드합니다.
```

---

## 8. 포스터 수정본을 다시 올리는 방법

같은 위치에 같은 파일명으로 다시 업로드하면 기존 파일이 새 파일로 교체됩니다.

예를 들어 기존 파일이 아래와 같다면:

```text
posters/web/poster-2026-04-web-main.jpg
```

수정본도 같은 파일명으로 저장합니다.

```text
poster-2026-04-web-main.jpg
```

그 다음 같은 위치에 업로드합니다.

```text
posters
→ web
→ Add file
→ Upload files
→ 수정본 드래그
→ Commit changes
```

그러면 공개 주소는 그대로 유지되고, 내용만 새 파일로 바뀝니다.

---

## 9. 포스터 업로드 후 확인할 것

업로드 후 다음 항목을 확인합니다.

```text
1. GitHub의 올바른 폴더에 파일이 들어갔는가
2. 파일명이 규칙에 맞는가
3. 공개 주소가 열리는가
4. 스마트폰에서도 열리는가
5. 이미지가 너무 무겁지 않은가
6. 인쇄용 파일은 해상도가 충분한가
7. source 폴더에 공개하면 안 되는 파일이 들어가지 않았는가
```

---

## 10. 권장 파일 크기

웹 게시용은 너무 크지 않게 만듭니다.

권장:

```text
1MB 이하 또는 2MB 이하
```

인쇄용은 품질이 중요하므로 더 커도 됩니다.

권장:

```text
PDF 또는 고해상도 PNG
```

단, GitHub에 너무 큰 파일을 많이 올리면 저장소 관리가 어려워질 수 있습니다.

---

## 11. 공개 전 주의사항

이 저장소는 공개 저장소입니다.

따라서 포스터를 올리기 전에 다음을 확인합니다.

```text
개인정보가 들어 있지 않은가
내부자료가 들어 있지 않은가
유료 폰트 파일이 포함되어 있지 않은가
저작권 문제가 있는 이미지 원본이 포함되어 있지 않은가
외부 공개가 가능한 자료인가
```

특히 `source` 폴더는 주의합니다.

---

## 12. 빠른 업로드 요약

웹 게시용 포스터를 올릴 때:

```text
1. 파일명 변경: poster-2026-04-web-main.jpg
2. GitHub 접속: https://github.com/libjeju/books
3. issues → 2026-04 → posters → web 이동
4. Add file → Upload files 클릭
5. 파일 드래그
6. Commit message 입력
7. Commit changes 클릭
8. 공개 주소 확인
```

인쇄용 포스터를 올릴 때:

```text
1. 파일명 변경: poster-2026-04-print-a4.pdf
2. GitHub 접속: https://github.com/libjeju/books
3. issues → 2026-04 → posters → print 이동
4. Add file → Upload files 클릭
5. 파일 드래그
6. Commit message 입력
7. Commit changes 클릭
8. 공개 주소 확인
```

원본 편집파일을 올릴 때:

```text
1. 공개 가능한 원본인지 확인
2. 파일명 변경: poster-2026-04-source.pptx
3. GitHub 접속: https://github.com/libjeju/books
4. issues → 2026-04 → posters → source 이동
5. Add file → Upload files 클릭
6. 파일 드래그
7. Commit changes 클릭
8. 공개해도 되는 파일인지 다시 확인
```
