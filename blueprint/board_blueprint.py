from flask import Blueprint, render_template, request, session
from database import board_dao, content_dao
import os
import time

board_blue = Blueprint("board", __name__)

# 게시글 리스트
@board_blue.route("/board_main")
def board_main():
    # 게시판 인덱스 파라미터 추출
    board_idx = request.args.get("board_idx")

    # 현재 페이지 파라미터 추출
    page = request.args.get("page")
    if not page:
        page = "1"
    page = int(page)

    # 페이지 번호가 0이하면
    if page < 1:
        page = 1

    # 게시글 전체 개수 가져오기
    contentCnt = content_dao.getContentCnt(board_idx)
    print(contentCnt)

    # 게시글 전체 개수를 이용해 전체 페이지 수 계산
    pageCnt = contentCnt // 10
    if contentCnt % 10 > 0:
        pageCnt += 1

    # 요청하는 페이지 번호가 전체 페이지 개수보다 크면 전체 페이지 개수로 넣어준다.
    if page > pageCnt:
        page = pageCnt

    # 한 페이지당 게시글의 개수
    content_count = 10

    # pagination 시작값
    start_page = (page - 1) // content_count * content_count + 1

    # pagination 종료값
    end_page = start_page + 9
    if end_page > pageCnt:
        end_page = pageCnt

    # 해당 인덱스의 정보 데이터 베이스에서 가져오기
    board_data = board_dao.selectBoardData(board_idx)
    # print(board_data)

    # 전체 게시글 목록 가져오기
    content_list = content_dao.selectAllContentData(board_idx, page, content_count)

    return render_template(
        "/board/board_main.html",
        board_data=board_data,
        content_list=content_list,
        board_idx=board_idx,
        start_page=start_page,
        current_page=page,
        end_page=end_page,
        page_cnt=pageCnt,
    )


# 게시글 보는 페이지
@board_blue.route("/board_read", methods=["get", "post"])
def board_read():
    # 파라미터 추출
    content_idx = request.args.get("content_idx")
    board_idx = request.args.get("board_idx")
    page = request.args.get("page")
    # print(content_idx, board_idx)

    # 현재 글 정보 가져온다.
    content_data = content_dao.selectContentData(content_idx)
    # print(content_data)

    # print(session.get("user_idx"), content_data[6])

    return render_template(
        "board/board_read.html",
        content_data=content_data,
        board_idx=board_idx,
        page=page,
        content_idx=content_idx,
    )


# 게시글 쓰는 페이지
@board_blue.route("/board_write")
def board_write():
    # 게시판 인덱스 파라미터 추출
    board_idx = request.args.get("board_idx")
    content_idx = request.args.get("content_idx")
    # print(board_idx)

    return render_template("board/board_write.html", board_idx=board_idx, content_idx=content_idx)


# 게시글 수정하는 페이지
@board_blue.route("/board_modify")
def board_modify():
    # 파라미터 추출
    content_idx = request.args.get("content_idx")
    board_idx = request.args.get("board_idx")
    page = request.args.get("page")
    # print(content_idx, board_idx, page)

    # 현재 글 정보 가져온다.
    content_data = content_dao.selectContentData(content_idx)
    # print(content_data)

    return render_template(
        "board/board_modify.html", content_data=content_data, content_idx=content_idx, board_idx=board_idx, page=page
    )


# 글 작성 처리
@board_blue.route("/board_write_pro", methods=["post"])
def board_write_pro():
    # 입력한 제목, 내용, 게시판 인덱스 번호 파라미터
    content_subject = request.form.get("content_subject")
    content_text = request.form.get("content_text")
    content_board_idx = request.form.get("board_idx")

    # 첨부한 파일이 있는 경우
    if request.files.get("content_file").filename:
        # content_file로 넘어오는 파일 데이터 추출
        content_file = request.files.get("content_file")
        # 중복 방지를 위해 파일 이름에 시간을 붙인다.
        file_name = str(int(time.time())) + content_file.filename
        # print(file_name)
        # 파일 저장할 경로
        file_path = os.getcwd() + "/static/upload/" + file_name
        # print(file_path)
        # 저장
        content_file.save(file_path)
    else:
        file_name = None

    # 유저 인덱스 번호 파라미터
    content_writer_idx = session.get("user_idx")
    # print(content_subject, content_writer_idx, content_text, file_name, content_board_idx)

    # 추출한 파라미터 데이터 베이스에 저장
    content_dao.insertContentData(content_subject, content_writer_idx, content_text, file_name, content_board_idx)

    # 방금 작성한 글의 인덱스를 가져온다.
    now_content_idx = content_dao.getMaxContentIdx(content_board_idx)
    # print(now_content_idx)

    return f"""
        <script>
            alert('작성 완료 되었습니다.')
            location.href = 'board_read?content_idx={now_content_idx}&board_idx={content_board_idx}'
        </script>
    """


# 게시글 삭제
@board_blue.route("/board_delete")
def board_delete():
    # 파라미터 추출
    content_idx = request.args.get("content_idx")
    board_idx = request.args.get("board_idx")
    page = request.args.get("page")
    # print(content_idx, board_idx, page)

    # 게시글 삭제
    content_dao.deleteContentData(content_idx)

    return f"""
        <script>
            alert('삭제 완료 되었습니다')
            location.href = 'board_main?board_idx={board_idx}&page={page}'
        </script>
    """


@board_blue.route("/board_modify_pro", methods=["post"])
def board_modify_pro():
    # 파라미터 추출
    board_idx = request.form.get("board_idx")
    page = request.form.get("page")
    content_idx = request.form.get("content_idx")
    content_subject = request.form.get("content_subject")
    content_text = request.form.get("content_text")
    # print(board_idx, page, content_idx, content_subject, content_text)

    # 첨부한 파일이 있는 경우
    if request.files.get("content_file").filename:
        # content_file로 넘어오는 파일 데이터 추출
        content_file = request.files.get("content_file")
        # 중복 방지를 위해 파일 이름에 시간을 붙인다.
        file_name = str(int(time.time())) + content_file.filename
        # print(file_name)
        # 파일 저장할 경로
        file_path = os.getcwd() + "/static/upload/" + file_name
        # print(file_path)
        # 저장
        content_file.save(file_path)
    else:
        file_name = None

    # 게시글 수정
    content_dao.updateContentData(content_idx, content_subject, content_text, file_name)

    return f"""
        <script>
            alert('수정 완료 되었습니다')
            location.href = 'board_read?content_idx={content_idx}&board_idx={board_idx}&page={page}'
        </script>
    """


# 첨부파일 삭제
@board_blue.route("/delete_img")
def delete_img():
    # 파라미터 추출
    content_idx = request.args.get("content_idx")
    # 첨부파일 삭제 -> null
    content_dao.updateContentImg(content_idx)

    return content_idx