# 🎞 영화 추천 웹사이트 구축 프로젝트

##### 주제: 그날 기분이나 상태:smiley:에 따른 영화 추천 알고리즘

>팀명: 지-드래곤
>팀원: 강용준, 홍지선



<img src="https://user-images.githubusercontent.com/60081206/85564317-1fd38a80-b669-11ea-8db4-763416d8b912.png" alt="image" style="zoom: 60%;" />



2020.06.10 ~ 2020.06.19

## 0. 팀원 정보 및 업무 분담 내역

- 강용준 : TDMB API를 활용한 DataBase 구축, 메인 기능 개발, 화면 UI 설계
- 홍지선 : 추천 알고리즘 아이디어, 세부기능/UI 개발, DB 설계, 프로젝트 정의서, 완료보고서 작성 



## 1. 프로젝트 목표

- 영화 정보 기반 추천 서비스를 제공하는 사이트를 구현한다.

- TMDB API를 사용해 seed data를 수집하고, 가공하여 데이터 베이스를 구축한다.

- `HTML`, `CSS`, `JavaScript`, `Django`, `REST API`, `DataBase` 등을 활용한 실제 서비스를 설계한다.

- `github`를 활용하여 소스코드 버전 관리를 진행한다.

  

## 2. 개발 환경

- Python Web Framework
  - A. Django 2.1.15
  - B. Python 3.7.3

- 개발 아키텍처
  - Django & Vanila JS
- Frontend
  - A. Font Awesome 5.8.2
  - B. Bootstrap 4.5
  - C. jQuery
- Database
  - sqlite3



## 3. 프로젝트 구조

- **프로젝트 개요 영상으로 보기 **:play_or_pause_button:

  https://www.youtube.com/watch?v=66BJpasheHM  (클릭 시 유튜브로 이동)

- 영화 정보 :  The Movie Database(TMDB) 영화 데이터 수집

- 추천 알고리즘 : 그날 기분을 고려한 영화 추천

- **프로젝트명**: `movie_pjt` / **앱명**: `accounts`, `movies`

  **1) accounts App**

  ​	① 회원가입 (`/accounts/signup/`)

  ​	② 로그인 (`/accounts/login/`)

  ​	③ 프로필 (`/accounts/<str:username>`/)

  ​	④ 팔로우 (`/accounts/<str:username>/follow/`)

  **2) movies App**

  ​	① 오늘의 기분 선택 페이지 (`/`)

  ​	② 영화 추천 목록 (`/movie_list/`)

  ​	③ 영화 최신순으로 정렬 (`/recent_movie/`)

  ​	④ 영화 디테일 정보 (`/<int:movie_pk>/`)

  ​	⑤ 영화 검색 (`/search/search_result`)

  ​	⑥ 커뮤니티 (`/review_list/`)

  ​	⑦ 리뷰 디테일 정보 (`/<int:movie_pk>/<int:review_pk>/)`

  **3) 기타**

  ​	①  `base.html` : bootstrap CDN, Font Awesome CDN, jquery CDN 삽입

  ​	②  `footer.html` : javascript onclick 이벤트 이용

- **프로젝트 폴더 구성**

  ```
  movie_pjt
  ├── README.md
  ├── accounts
  │   ├── migrations
  │   ├── static\accounts\images
  │   │       ├── google_login.png
  │   │       └── naver_login.png
  │   ├── templates\accounts
  │   │       ├── login.html
  │   │       ├── profile.html
  │   │       ├── profile_update.html
  │   │       └── signup.html
  │   ├── admin.py
  │   ├── apps.py
  │   ├── forms.py
  │   ├── models.py
  │   ├── tests.py
  │   ├── urls.py
  │   └── views.py
  ├── movie_pjt
  │   ├── settings.py
  │   ├── urls.py
  │   └── wsgi.py
  ├── movies
  │   ├── fixtures\movies
  │   │   ├── cast.json
  │   │   ├── emotion.json
  │   │   ├── genre.json
  │   │   └── movie.json
  │   ├── migrations
  │   ├── static\movies\css
  │   │   └── movie_list.css
  │   ├── templates\movies
  │   │   ├── first_page.html
  │   │   ├── form.html
  │   │   ├── movie_detail.html
  │   │   ├── movie_list.html
  │   │   ├── recent_movie.html
  │   │   ├── review_detail.html
  │   │   ├── review_list.html
  │   │   └── search_result.html
  │   ├── admin.py
  │   ├── apps.py
  │   ├── forms.py
  │   ├── models.py
  │   ├── tests.py
  │   ├── urls.py
  │   └── views.py
  ├── static\images
  ├── templates
  │   ├── base.html
  │   └── footer.html
  ├── .gitignore
  ├── db.sqlite3
  ├── manage.py
  └── requirements.txt
  ```



## 4. 데이터베이스 모델링(ERD)

- erdcloud(www.erdcloud.com)를 이용해 실제 모델링 전, 데이터베이스 모델링을 진행함.

<img src="https://user-images.githubusercontent.com/60081206/85927835-ab585000-b8e3-11ea-90fb-44ed2be28eac.png" alt="image" style="zoom:80%;" />



## 5. 목표 서비스 및 실제 구현 정도

#### 1) 회원 가입 및 로그인 기능

- 회원가입 기능 
  - 사용자 이름, 비밀번호, 비밀번호 확인, 닉네임 입력
- 로그인 
  - 사이트 내 가입한 아이디로 로그인
  - 소셜로그인 기능 구현 (구글, 네이버, 페이스북 중 페이스북은 구현하지 못했음)
  - 회원가입 안했을 경우 바로 회원가입 페이지로 이동하도록 링크 삽입

<img src="https://user-images.githubusercontent.com/60081206/85592608-47365180-b681-11ea-9fb3-115dcc597971.png" alt="image" style="zoom:50%;" />

<img src="https://user-images.githubusercontent.com/60081206/85592380-15bd8600-b681-11ea-8e81-aa47194f1fb8.png" alt="image" style="zoom:50%;" />



#### 2) 영화 추천 서비스

- 메인 화면에서 5가지 기분과 기분에 따른 2가지 카드 선택지 제공
- 선택한 카드에 따라 영화 트레일러와 비슷한 장르의 영화 15개 추천
  - 유튜브 API를 활용해 트레일러 연결
- 추가적으로 리뷰가 많은 영화를 함께 추천

<img src="https://user-images.githubusercontent.com/60081206/85644233-59d87700-b6d1-11ea-9f2b-11555753caee.png" alt="image" style="zoom:40%;" />

<img src="https://user-images.githubusercontent.com/60081206/85644325-8b514280-b6d1-11ea-9bd0-170ba4fb813d.png" alt="image" style="zoom:40%;" />

<img src="https://user-images.githubusercontent.com/60081206/85644523-26e2b300-b6d2-11ea-83b2-c8dd0e980055.png" alt="image" style="zoom:40%;" />

<img src="https://user-images.githubusercontent.com/60081206/85644561-44b01800-b6d2-11ea-9886-78b9d49d87f5.png" alt="image" style="zoom:40%;" />



#### 3) 최신 영화순 / 영화 디테일

- 영화를 최신순으로 정렬하여 제공
- 영화 선택 시, 영화 디테일 정보 제공
  - 줄거리, 디테일 정보, 출연 배우, 관련 영화 정보
  - 영화 포스터 클릭 시, 트레일러를 `modal`로 제공
  - 영화에 대해 별점으로 평점 매기는 기능
  - 해당 영화 좋아요 가능 -> 프로필 페이지에서 좋아요 한 영화 리스트 확인 가능
- 영화에 대한 리뷰 모아서 게시판 형태로 제공
  - 리뷰 작성도 가능
  - 리뷰 제목, 내용, 작성일자 제공

<img src="https://user-images.githubusercontent.com/60081206/85646772-d2423680-b6d7-11ea-8560-2fd67a284edb.png" alt="image" style="zoom:32%;" />

<img src="https://user-images.githubusercontent.com/60081206/85644850-154ddb00-b6d3-11ea-8c61-b87e03801a29.png" alt="image" style="zoom:40%;" />

<img src="https://user-images.githubusercontent.com/60081206/85645014-88575180-b6d3-11ea-8eb8-242b57ed74b0.png" alt="image" style="zoom:40%;" />



#### 4) 커뮤니티 (리뷰, 코멘트)

- 커뮤니티
  - 유저들이 쓴 리뷰들을 목록으로 확인 가능
  - 영화 제목, 리뷰 제목, 별점, 작성자, 작성 시간, 수정 시간 노출 (사용자 편의성 도모)
  - `영화 제목` 클릭 시 -> 영화 디테일 페이지로 이동
  - `리뷰 제목` 클릭 시 -> 해당 리뷰 디테일로 이동
  - `작성자` 클릭 시 -> 작성자 프로필로 이동
  - 페이지네이션 기능 추가
    - 커뮤니티 글을 5개씩 보여줄 수 있도록 페이지네이션 기능 추가
- 리뷰 디테일 페이지
  - 리뷰 제목, 작성자 정보, 작성일자
  - `{작성자} 님의 모든 리뷰 보기` 클릭 시 -> 작성자 프로필로 이동
  - `목록으로 돌아가기` 클릭 시 -> 커뮤니티로 이동
  - `이 영화 보러가기` 클릭 시 -> 영화 디테일 페이지로 이동
- 코멘트 기능
  - 리뷰에 코멘트를 남길 수 있는 기능 제공
    - 작성자 이름, 코멘트 내용, 작성 시간 + 본인의 댓글일 경우 삭제 기능 제공
- 유저 프로필 페이지
  - 유저가 남긴 게시글 수, 팔로우한 유저, 유저를 팔로잉하는 유저 정보 제공
  - `이런 영화에 관심이 있어요`에서 유저가 남긴 리뷰를 영화 포스터, 영화 제목, 리뷰 제목과 함께 보여줌. 
  - `리뷰 읽기`를 클릭 시 -> 해당 리뷰로 이동
  - 팔로우 버튼 제공
  - 본인 프로필 페이지에서 유저 정보 수정 가능

<img src="https://user-images.githubusercontent.com/60081206/85646396-f94c3880-b6d6-11ea-9ac0-827548d0387b.png" alt="image" style="zoom:35%;" />

<img src="https://user-images.githubusercontent.com/60081206/85646642-7f687f00-b6d7-11ea-9b55-ef14f30123ea.png" alt="image" style="zoom:35%;" />

<img src="https://user-images.githubusercontent.com/60081206/85646983-5ac0d700-b6d8-11ea-9d1e-642486025205.png" alt="image" style="zoom:35%;" />



#### 5) 기타

- **nav bar**

  - 좌측: `홈`, `최신 영화` 목록, `커뮤니티`(리뷰), `추천 다시받기`로 구성 

  - 우측:
    로그인 정보 없을 시 - `로그인` | `회원 가입` 노출		![image](https://user-images.githubusercontent.com/60081206/85922216-987e5500-b8bc-11ea-8abe-b69c8c808127.png)
    
    로그인 시 -  `'유저 닉네임' 님 안녕하세요!`(유저 정보) | `로그아웃` 노출![image](https://user-images.githubusercontent.com/60081206/85648401-a6c14b00-b6db-11ea-8b4c-7e77feb2f710.png)

- **영화 검색창 기능**

  - nav bar 우측에 위치한 검색창에 단어를 검색할 경우, 영화의 제목과 줄거리에 해당 단어가 포함된 검색결과를 보여줌

  <img src="https://user-images.githubusercontent.com/60081206/85647514-94461200-b6d9-11ea-9971-bb94ec211958.png" alt="image" style="zoom:40%;" />

- **footer**

  - `오늘영화` 에 대한 간단한 소개 글
  - `사이트 링크`를 통해 해당 페이지로 바로가기 기능 제공
  - `연락처`를 통해 질문이나, 전화번호를 남겨 바로 문의를 남길 수 있도록 함. 문의 메일 주소 클릭 시 G-mail 메일 보내기로 연결
  - jquery를 이용해 웹사이트 최상단으로 이동하는 버튼(:top:)을 만들어둠.  직관적인 UI로 구상함.

  <img src="https://user-images.githubusercontent.com/60081206/85644947-5219d200-b6d3-11ea-85de-1610429d319f.png" alt="image" style="zoom:50%;" />

  <img src="https://user-images.githubusercontent.com/60081206/85922469-78e82c00-b8be-11ea-8b6a-42ecc0b594a2.png" alt="image" style="zoom: 64%;" />

- 로그인 이슈 ( 로그인이 되어 있는 상태로 git에 올라가게 됨. )

  - 자동 로그 아웃 기능 추가

  ```python
  SESSION_COOKIE_AGE = 300
  SESSION_SAVE_EVERY_REQUEST = True
  ```



## 6. 프로젝트를 통해 느낀 점

- **강용준**
  - 최종 프로젝트를 진행하기 전 5차 장고 프로젝트에서 로그인이 되어있는 상태에서 git push를 하게 되면 clone이나 pull을 받는 사람은 회원정보가 없는데 로그인이 되어있는 상태라 페이지 이용에 문제가 생기게 되었었음. 로그인 되어있는 상태로 요청을  5분 이상 보내지 않는다면  자동 로그아웃이 되게 되어 이런 문제를 해결하려 함.
- **홍지선**
  - 프로젝트를 진행하면서 필드를 몇번 바꾸는 일이 생겼고, 번번이 마이그레이션을 다시해야했기에 초기 모델링의 중요성을 깨달았음.
  - 프로필 페이지 CSS를 작성하면서 position과 배치 등 스케치로 구상해둔 것을 직접 구현하면서 속성에 대해 깊이 이해할 수 있었음. 다만, 사용자의 디스플레이 환경을 고려하지 못한 점이 숙제로 남았음. 다음 프로젝트에서는 반응형 웹을 고려하고 싶음.



## 7. 프로젝트 Executive Summary

<img src="https://user-images.githubusercontent.com/60081206/85566626-2b27b580-b66b-11ea-856b-e29c3c6668aa.png" alt="image" style="zoom: 60%;" />

<img src="C:\Users\zs781\AppData\Roaming\Typora\typora-user-images\image-20200624223937899.png" alt="image-20200624223937899" style="zoom:60%;" />

