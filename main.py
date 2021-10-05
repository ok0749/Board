from flask import Flask, redirect, url_for

from blueprint.main_blueprint import main_blue
from blueprint.board_blueprint import board_blue
from blueprint.user_blueprint import user_blue


# 서버 역할을 할 객체 생성
# template_foler: 랜더링할 html 문서가 있는 곳(기본 - templates)
# static_folder: 정적 파일이 있는 곳(기본 - static)
app = Flask(__name__, template_folder="views", static_folder="static")

# 세션영역 사용을 위한 암호화 키 설정
app.secret_key = "rueowqjvcxzvdija"

# blueprint 등록
app.register_blueprint(main_blue)
app.register_blueprint(board_blue)
app.register_blueprint(user_blue)

# 홈
@app.route("/")
def index():
    # 브라우저에게 main을 요청하라는 응답 결과를 전달한다.
    # 주소만 치면 주소/main으로 이동
    return redirect("main")


# 서버 가동
# port=80: 요청할 때 포트번호 생략하고 호출 가능
# debug=True: 코드 수정하면 서버 재가동 -> 서비스할 때는 지워야한다.
if __name__ == "__main__":
    app.run(port=5000, debug=True)