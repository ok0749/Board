# Board
## 배경
  - Python, Flask, MariaDB, Bootstrap을 사용하여 게시판 웹 구현

## 작업내용
  - Flask 프레임워크를 사용해 유저 관련 API(Login, Join 등), 게시판 관련 API(Read, Write 등) 구현
  - 데이터베이스에 Board_table, Content_table, User_table을 생성한다 Content_table에는 Content_board_idx 항목을 통해 Board_table과 연결하고(콘텐츠가 어떤 게시판에 해당되는지) Content_writer_idx 항목을 통해 User_table과 연결(어떤 유저가 콘텐츠를 작성했는지)
  - Board_main
    - 게시판 별로 최신글 다섯개를 보여주도록 구현
  - Board_read
    - 페이지당 10개 글 보여주도록 설정, Pagination 구현
  - Board_write
    - 첨부된 이미지 파일은 /static/upload 폴더에 저장하고 데이터베이스에는 파일명만 저장하도록 구현(게시판 글을 읽을 때 파일명을 통해서 이미지 파일을 불러온다)
  - Board_modify
    - 로그인된 유저와 작성한 유저가 동일할 경우 수정 버튼 보이도록 구현
    - 수정 및 삭제 가능하도록 구현

## 사용기술
  - Python
  - Flask
  - Pymysql
  - Bootstrap
  - MariaDB
  
## 로컬에서 실행 방법
    python main.py
