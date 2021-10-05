# dao: database access object
# CRUD를 미리 만들어 놓는다. -> 나중에 편하기 위해서

from database import connector

# 사용자 정보 저장하는 함수
def insertUserData(user_name, user_id, user_pw):
    # 쿼리문
    # 데이터 타입과 관계없이 %s로 준다 %d 등 다른 값을 주면 에러날 수도 있다.
    sql = """
        insert into user_table(user_name, user_id, user_pw) values (%s, %s, %s)
    """

    # 데이터베이스 접속
    conn = connector.get_connection()
    cursor = conn.cursor()

    # %s 부분에 대입될 값을 튜플로 생성(괄호 생략시 튜플로 생성 된다.)
    # 쿼리문의 %s 순서에 맞춰 값을 준다.
    data = user_name, user_id, user_pw

    # 쿼리문 실행
    cursor.execute(sql, data)
    conn.commit()

    # 데이터베이스 접속 해제
    conn.close()


# 모든 회원 정보를 반환하는 함수
def selectUserDataAll():
    # 쿼리문
    sql = """
        select * from user_table
    """

    # 데이터베이스 접속
    conn = connector.get_connection()
    cursor = conn.cursor()

    # 쿼리문 실행
    cursor.execute(sql)
    result = cursor.fetchall()

    # 데이터베이스 접속 해제
    conn.close()

    return result


# 회원 한명의 데이터를 가져오는 함수
def selectUserDataOne(user_idx):
    # 쿼리문
    sql = """
        select * from user_table where user_idx = %s
    """

    # 데이터 베이스 접속
    conn = connector.get_connection()
    cursor = conn.cursor()

    # %s에 대입될 값 지정
    data = (user_idx,)

    # 쿼리문 실행
    cursor.execute(sql, data)
    result = cursor.fetchone()

    # 데이터 베이스 접속 해제
    conn.close()

    return result


# 특정 회원의 데이터 업데이트 하는 함수
# 이름과 아이디는 수정 못하게 한다. -> 비밀번호만 수정 가능
def updateUserData(user_idx, user_pw):
    # 쿼리문
    sql = """
        update user_table 
        set user_pw = %s 
        where user_idx = %s
    """
    # 데이터 베이스 접속
    conn = connector.get_connection()
    cursor = conn.cursor()

    # 대입할 값
    data = (user_pw, user_idx)

    # 쿼리문 실행
    cursor.execute(sql, data)
    conn.commit()

    # 데이터 베이스 접속 종료
    conn.close()


# 회원 정보 삭제 함수
def deleteUserData(user_idx):
    # 쿼리문
    sql = """
        delete from user_table 
        where user_idx= %s
    """

    # 접속
    conn = connector.get_connection()
    cursor = conn.cursor()

    # 대입할 값
    data = user_idx

    # 쿼리문 실행
    cursor.execute(sql, data)
    conn.commit()

    # 접속 해제
    conn.close()


# 회원 가입시 사용자가 입력한 아이디 중복 확인
def checkInputUserId(new_id):
    # 쿼리문
    sql = """
        select * from user_table
        where user_id = %s
    """
    # 접속
    conn = connector.get_connection()
    cursor = conn.cursor()
    # 데이터
    data = new_id
    # 쿼리문 실행
    cursor.execute(sql, data)
    result = cursor.fetchone()
    # 접속 해제
    conn.close()
    # 아이디 사용 가능하면 True 반환, 중복이면 False 반환
    if not result:
        return True
    else:
        return False


# 로그인 처리를 위해 회원 정보 확인
def checkLoginUser(user_id, user_pw):
    # 쿼리문
    sql = """
        select * from user_table
        where user_id = %s and user_pw = %s
    """
    # 접속
    conn = connector.get_connection()
    cursor = conn.cursor()
    # 데이터
    data = (user_id, user_pw)
    # 쿼리문 실행
    cursor.execute(sql, data)
    result = cursor.fetchone()
    # 접속 해제
    conn.close()

    return result