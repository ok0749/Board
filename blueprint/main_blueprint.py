from flask import Blueprint, render_template, session
from database import board_dao, content_dao

# 블루 프린트 객체 생성
main_blue = Blueprint("main", __name__)

# 홈 화면
@main_blue.route("/main")
def main():

    # 게시판 이름 정보를 가져온다.
    board_data = board_dao.selectAllBoardData()
    # print(board_data)

    # 게시판별 상위 5개의 게시글의 데이터 담을 리스트
    content_list = []

    # 5개
    content_count = 5

    for board_idx, _ in board_data:
        # 게시판별 첫 페이지 게시글 가져온다.
        contents = content_dao.selectAllContentData(board_idx, 1, content_count)
        content_list.append(contents)
        # print(content_list)

    return render_template("/main/main.html", board_data=board_data, content_list=content_list)
