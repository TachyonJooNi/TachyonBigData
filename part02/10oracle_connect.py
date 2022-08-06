# -*- coding: utf-8 -*-

# 오라클 사용을 위해 cx_Oracle라이브러리 설치가 필요하다.
import cx_Oracle as cx

# 오라클 접속 정보 및 계정 정보
host_name = 'localhost'
oracle_port = 1521
service_name = 'xe'
connect_info = cx.makedsn(host_name, oracle_port, service_name)
# 오라클 접속
conn = cx.connect('musthave', '1234', connect_info)
# 쿼리 실행을 위해 cursor객체를 생성한다.
# --파이썬?? 오라클?? 은 커서를 통해서 sql에 접근한다.
cursor = conn.cursor()

# 인파라미터가 없는 쿼리문
sql = "select * from member"
cursor.execute(sql)
print("전체회원출력")
# 회원수만큼 반복해서 출력한다.
for rs in cursor:
    # 컬럼에 접근할때는 인덱스 0부터 시작한다.
    print(rs[0], rs[1], rs[2], rs[3])

# 인파라미터가 있는 쿼리문
# 쿼리문에  :변수명 과 같이 기술한 후 execute()에서 값을 설정한다.
sql = "select * from member where id=:userid"
# 쿼리 실행시 인파라미터를 설정한다.
cursor.execute(sql, userid='test1')
# fetchone() : 하나의 레코드를 인출(추출)한다.
member = cursor.fetchone()
print("\ntest1 회원출력")
print("%s %s %s %s" % (member[0], member[1], member[2], member[3]))

# 인서트
my_tit = "셀레니움 크롤링 좋아요"
my_con = "크롤링 엄청 잘되"
my_id = "musthave"
# 두줄 이상의 문자열은 블럭단위 주석을 쓸때와 동일하게 기술한다.
sql = """insert into board (num, title, content, id, postdate, visitcount)
    values (seq_board_num.nextval, :title, :content, :userid, sysdate, 0)"""
    
try:
    # 쿼리 실행시 인파라미터 설정
    cursor.execute(sql, title=my_tit, content=my_con, userid=my_id)
    # 실행에 문제가 없다면 실제 테이블에 반영한다.
    conn.commit()
    print("1개의 레코드 입력")
except Exception as e:
    # 예외가 발생하면 롤백처리 한다.
    conn.rollback()
    print("insert 실행시 오류발생", e)
# insert, update, delete 계열의 쿼리문은 반드시 commit()을 해줘야한다.
# 연결 해
conn.close()
