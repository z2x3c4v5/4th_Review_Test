# Lesson 7 영어 공부방

4학년 Lesson 7 *Writing Words and Sentences* (Is this your cap?) 시험 대비용 웹 앱.

- **① 단어**: 단어 카드를 누르면 그 단어 소리가 나옴, 전체 듣기
- **② 문장**: 20개 단어 각각이 들어간 문장 듣기 / 천천히 듣기
- **③ 빈칸 채우기**: 시험지 1~20번을 빈칸으로 보여 줌. 학생은 공책에 답을 적음 (입력·채점 없음). 문제마다 "정답 보기", 위에 "정답 모두 보기"

`index.html` 하나만 열면 됩니다 (그림 포함). 소리는 브라우저 내장 음성(Web Speech)을 사용합니다.

## 수정하기
`app.html`(화면·문제 데이터 `ITEMS`)과 `images/`를 고친 뒤 `python3 build.py`로 `index.html`을 다시 만듭니다.
