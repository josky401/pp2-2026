# 파일명: week4/programming/prob6.py
# 작성자: 조하늘
# 작성일: 2026-10-03
# 문제: Person 클래스 구현 (파이썬 익스프레스 06번)
# 설계:
#   - Person 클래스: name, mobile, office, email 속성 (기본값 지원)
#   - 메서드: __init__, __str__, 각 속성에 대한 getter/setter 함수들
#   - test_prob6(): 문제 조건에 맞는 객체 생성 및 setter/getter/str 동작 검증

class Person:
    def __init__(self, name, mobile=None, office=None, email=None):
        self.name = name
        self.mobile = mobile
        self.office = office
        self.email = email

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getMobile(self):
        return self.mobile

    def setMobile(self, mobile):
        self.mobile = mobile

    def getOffice(self):
        return self.office

    def setOffice(self, office):
        self.office = office

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email

    def __str__(self):
        return f"Person(name={self.name}, mobile={self.mobile}, office={self.office}, email={self.email})"


def test_prob6():
    p1 = Person("Kim", office="1234567", email="kim@company.com")
    print("p1:", p1)

    p2 = Person("Park", office="2345678")
    print("p2 (변경 전):", p2)

    p2.setEmail("park@company.com")
    print("p2 (setEmail 후):", p2)


if __name__ == "__main__":
    test_prob6()