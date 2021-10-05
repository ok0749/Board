from database import connector


# 게시판 정보 저장
def insertBoardData(board_name):
    # 쿼리문
    sql = """
        insert into board_table(board_name) values (%s)
    """
    # 접속
    conn = connector.get_connection()
    cursor = conn.cursor()
    # 대입할 값
    data = board_name
    # 쿼리문 실행
    cursor.execute(sql, board_name)
    conn.commit()
    # 접속 해제
    conn.close()


# 게시판 정보 모두 가져오기
def selectAllBoardData():
    # 쿼리문
    # board_idx 기준으로 오름차순 정렬
    sql = """
        select * from board_table
        order by board_idx
    """
    # 접속
    conn = connector.get_connection()
    cursor = conn.cursor()
    # 쿼리문 실행
    cursor.execute(sql)
    result = cursor.fetchall()
    # 접속 해제
    conn.close()

    return result


# 특정 게시판 정보 가져오기
def selectBoardData(board_idx):
    # 쿼리문
    sql = """
        select * from board_table where board_idx = %s
    """
    # 접속
    conn = connector.get_connection()
    cursor = conn.cursor()
    # 대입할 값
    data = board_idx
    # 쿼리문 실행
    cursor.execute(sql, data)
    result = cursor.fetchone()
    # 접속 해제
    conn.close()

    return result


# 특정 게시판 정보 수정
def updateBoardData(board_idx, board_name):
    # 쿼리문
    sql = """
        update board_table
        set board_name = %s
        where board_idx = %s
    """
    # 접속
    conn = connector.get_connection()
    cursor = conn.cursor()
    # 대입할 데이터
    data = (board_name, board_idx)
    # 쿼리문 실행
    cursor.execute(sql, data)
    conn.commit()
    # 접속 해제
    conn.close()


# 특정 게시판 정보 삭제
def deleteBoardData(board_idx):
    # 쿼리문
    sql = """
        delete from board_table
        where board_idx = %s
    """
    # 접속
    conn = connector.get_connection()
    cursor = conn.cursor()
    # 대입할 데이터
    data = board_idx
    # 쿼리문 실행
    cursor.execute(sql, data)
    conn.commit()
    # 접속 해제
    conn.close()
