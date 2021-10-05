from flask import Blueprint, render_template, redirect, request, session
from database import user_dao

user_blue = Blueprint("user", __name__)

# 사용자 로그인
@user_blue.route("/user_login")
def user_login_fail():
    # 파라미터 데이터 추출
    login_fail = request.args.get("login_fail")
    # 응답 결과 랜더링
    return render_template("user/user_login.html", login_fail=login_fail)


# 로그인
@user_blue.route("/user_login")
def user_login():
    return render_template("user/user_login.html")


# 회원가입
@user_blue.route("/user_join")
def user_join():
    return render_template("user/user_join.html")


# 회원 정보 수정
@user_blue.route("/user_modify")
def user_modify():
    # 세션에 저장된 사용자 인덱스 번호
    user_idx = session.get("user_idx")

    # 로그인 하지 않았다면 로그인 페이지로 강제 이동
    # 로그인 하지 않고 직접 주소 치고 들어오는 것 막는다
    if not user_idx:
        return """
            <script>
                alert('로그인 해주세요')
                location.href = 'user_login'
            </script>
        """

    # 로그인한 사용자 정보 가져온다
    user_data = user_dao.selectUserDataOne(user_idx)
    # print(user_data)

    return render_template("user/user_modify.html", user_data=user_data)


# 로그아웃
@user_blue.route("/user_logout")
def user_logout():
    # 세션에서 유저 번호를 지워서 로그아웃
    session.pop("user_idx")

    return redirect("main")


# 회원 가입 처리
@user_blue.route("/user_join_pro", methods=["post"])
def user_join_pro():
    # 브라우저가 전달한 데이터 추출(이름, 아이디, 비밀번호)
    user_name = request.form.get("user_name")
    user_id = request.form.get("user_id")
    user_pw = request.form.get("user_pw")
    # print(user_name, user_id, user_pw)

    # 데이터 베이스에 유저 정보 저장
    user_dao.insertUserData(user_name, user_id, user_pw)

    return """
        <script>
            alert('가입이 완료되었습니다.')
            location.href = 'user_login'    
        </script>
    """


# 회원 가입시 아이디 중복 확인
@user_blue.route("/check_join_id")
def check_join_id():
    # 브라우저가 전달한 데이터 추출
    new_id = request.args.get("new_id")
    # 중복 확인
    result = user_dao.checkInputUserId(new_id)

    return f"{result}"


# 로그인 처리
@user_blue.route("/user_login_pro", methods=["post"])
def user_login_pro():
    # 브라우저가 전달한 데이터 추출
    user_id = request.form.get("user_id")
    user_pw = request.form.get("user_pw")
    # print(user_id, user_pw)

    # 회원 정보 확인
    # 회원 존재하면 정보가 반환되고 없으면 None 반환
    result = user_dao.checkLoginUser(user_id, user_pw)
    # print(result)

    # 로그인 실패
    if not result:
        return """
            <script>
                alert('로그인에 실패하셨습니다.')
                location.href = 'user_login?login_fail=true'
            </script>
        """
    # 로그인 성공
    else:
        # 세션에 로그인한 사용자의 번호를 담는다
        session["user_idx"] = result[0]

        return """
            <script>
                alert('로그인에 성공하셨습니다.')
                location.href = 'main'
            </script>
        """


# 사용자 정보 수정
@user_blue.route("/user_modify_pro", methods=["post"])
def user_modify_pro():
    # 파라미터 데이터 추출
    user_pw = request.form.get("user_pw")
    # print(user_pw)

    # 세션에서 로그인한 사용자의 인덱스를 가져온다
    user_idx = session.get("user_idx")
    # print(user_idx)

    # 수정한 정보 데이터 베이스에 업데이트
    user_dao.updateUserData(user_idx, user_pw)

    return """
        <script>
            alert('회원 정보가 수정되었습니다')
            location.href = 'user_modify'
        </script>
    """
