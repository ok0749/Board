from database import user_dao, board_dao, content_dao

# 사용자 정보 저장 테스트
# user_dao.insertUserData("홍길동", "abcd", 1234)
# user_dao.insertUserData("김일한", "aaaa", 1234)
# user_dao.insertUserData("윤정수", "bbbb", 1234)
# print("저장완료")

# 모든 사용자 정보 가져오는 테스트
# result = user_dao.selectUserDataAll()
# print(result)

# 회원 한명의 데이터를 가져오는 테스트
# result = user_dao.selectUserDataOne(2)
# print(result)

# 특정 회원의 비밀번호 수정하는 테스트
# user_dao.updateUserData(2, 123)
# result = user_dao.selectUserDataOne(2)
# print(result)

# 사용자 한명의 정보 삭제 테스트
# user_dao.deleteUserData(1)
# result = user_dao.selectUserDataOne(2)
# print(result)


# 게시판 정보 저장 테스트
# board_dao.insertBoardData("hello table")

# 게시판 정보 모두 가져오기
# result = board_dao.selectAllBoardData()
# print(result)

# 특정 게시판 정보 가져오기
# print(board_dao.selectBoardData(1))

# 특정 게시판 정보 업데이트
# board_dao.updateBoardData(1, "hi table")
# print(board_dao.selectBoardData(1))

# 특정 게시판 정보 삭제
# board_dao.deleteBoardData(1)
# print(board_dao.selectBoardData(1))

# 게시글 정보 저장
# content_dao.insertContentData("테스트 제목", 2, "테스트 내용", "aaa.jpg", 2)


# 전체 게시글 정보 불러오기
# print(content_dao.selectAllContentData())

# 특정 게시글 정보 불러오기
# print(content_dao.selectContentData(1))

# 특정 게시글 수정
# content_dao.updateContentData(1, "수정된 제목", 2, "수정된 내용", "bbb.jpg", 2)
# print(content_dao.selectContentData(1))

# 특정 게시글 삭제
# content_dao.deleteContentData(1)
# print(content_dao.selectContentData(1))