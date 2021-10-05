from database import connector

# 기본으로 CRUD 구성하고 필요하면 수정한다.

# 게시글 저장
def insertContentData(content_subject, content_writer_idx, content_text, content_file, content_board_idx):
    # 쿼리문
    # sysdate(): sql문이 호출되는 시점의 시간
    sql = """
        insert into content_table(content_subject, content_date, content_writer_idx, content_text, content_file, content_board_idx)
        values (%s, sysdate(), %s, %s, %s, %s)
    """
    # 접속
    conn = connector.get_connection()
    cursor = conn.cursor()
    # 데이터
    data = (content_subject, content_writer_idx, content_text, content_file, content_board_idx)
    # 쿼리문 실행
    cursor.execute(sql, data)
    conn.commit()
    # 접속 해제
    conn.close()


# 전체 게시글 정보 불러오기
def selectAllContentData(content_board_idx, page, content_count):
    # 페이징 -> limit 시작위치, 개수
    # 페이지 번호에 따른 시작 위치 계산
    page_num = (page - 1) * content_count
    # 쿼리문
    sql = """
        SELECT a1.content_idx, a1.content_subject, a2.user_name, a1.content_date
        FROM content_table a1, user_table a2 
        WHERE a1.content_writer_idx = a2.user_idx 
        AND a1.content_board_idx=%s
        ORDER BY a1.content_idx DESC
        limit %s, %s
    """
    # 접속
    conn = connector.get_connection()
    cursor = conn.cursor()
    # 데이터
    data = (content_board_idx, page_num, content_count)
    # 쿼리문 실행
    cursor.execute(sql, data)
    result = cursor.fetchall()
    # 접속 해제
    conn.close()

    return result


# 특정 게시글 정보 불러오기
def selectContentData(content_idx):
    # 쿼리문
    sql = """
        SELECT a2.user_name, a1.content_date, a1.content_subject, 
               a1.content_text, a1.content_file, a1.content_writer_idx, a2.user_idx
        FROM content_table a1, user_table a2 
        WHERE a1.content_writer_idx = a2.user_idx 
        AND a1.content_idx=%s
    """
    # 접속
    conn = connector.get_connection()
    cursor = conn.cursor()
    # 데이터
    data = (content_idx,)
    # 쿼리문 실행
    cursor.execute(sql, data)
    result = cursor.fetchone()
    # 접속 해제
    conn.close()

    return result


# 게시글 첨부파일 삭제
def updateContentImg(content_idx):
    sql = """
        UPDATE content_table SET content_file = NULL WHERE  content_idx=%s;
    """
    conn = connector.get_connection()
    cursor = conn.cursor()

    data = (content_idx,)

    cursor.execute(sql, data)
    conn.commit()

    conn.close()


# 특정 게시글 수정
def updateContentData(content_idx, content_subject, content_text, content_file):
    # 쿼리문
    # 첨부 이지미가 있는 경우와 없는 경우로 나눈다.
    # 첨부 파일 없다면 제목과 내용만 업데이트 한다
    sql = """
        update content_table 
        set content_subject = %s, 
            content_text = %s
        where content_idx = %s
    """
    # 접속
    conn = connector.get_connection()
    cursor = conn.cursor()
    # 데이터
    data = (content_subject, content_text, content_idx)
    # 쿼리문 실행
    cursor.execute(sql, data)

    # 첨부 파일이 있다면 첨부 파일도 업데이트 한다
    if content_file != None:
        sql2 = """
            update content_table
            set content_file = %s
            where content_idx = %s
        """

        data2 = (content_file, content_idx)
        cursor.execute(sql2, data2)

    conn.commit()
    # 접속 해제
    conn.close()


# 특정 게시글 삭제
def deleteContentData(content_idx):
    # 쿼리문
    sql = """
        delete from content_table
        where content_idx = %s
    """
    # 접속
    conn = connector.get_connection()
    cursor = conn.cursor()
    # 데이터
    data = (content_idx,)
    # 쿼리문 실행
    cursor.execute(sql, data)
    conn.commit()
    # 접속 해제
    conn.close()


# 방금 작성한 글의 인덱스 번호(인덱스 번호가 가장 큰 것)를 가져온다
def getMaxContentIdx(content_board_idx):
    # 쿼리문
    sql = """
        select max(content_idx)
        from content_table
        where content_board_idx = %s
    """
    # 접속
    conn = connector.get_connection()
    cursor = conn.cursor()
    # 데이터
    data = (content_board_idx,)
    # 쿼리문 실행
    cursor.execute(sql, data)
    result = cursor.fetchone()
    # 접속 해제
    conn.close()

    return result[0]


# 전체 글의 개수를 가져오는 함수
def getContentCnt(content_board_idx):
    # 쿼리문
    sql = """
        select count(*) from content_table
        where content_board_idx=%s
    """
    # 접속
    conn = connector.get_connection()
    cursor = conn.cursor()
    # 데이터
    data = (content_board_idx,)
    # 쿼리문 실행
    cursor.execute(sql, data)
    result = cursor.fetchone()
    # 접속 해제
    conn.close()

    return result[0]
