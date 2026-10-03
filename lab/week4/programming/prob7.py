# 파일명: week4/programming/prob7.py
# 작성자: 조하늘
# 작성일: 2026-10-03
# 문제: PhoneBook 클래스 구현 (파이썬 익스프레스 07번)
# 설계:
#   - PhoneBook 클래스: contacts 딕셔너리 속성
#   - 메서드: __init__, __str__, add()
#   - test_prob7(): PhoneBook 객체 생성, 연락처 추가 및 전체 목록 출력 검증

class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add(self, name, mobile=None, office=None, email=None):
        self.contacts[name] = {
            "mobile": mobile,
            "office": office,
            "email": email
        }

    def __str__(self):
        result = "PhoneBook Contacts:\n"
        for name, info in self.contacts.items():
            result += f" - {name}: mobile={info['mobile']}, office={info['office']}, email={info['email']}\n"
        return result.strip()


def test_prob7():
    phone_book = PhoneBook()

    phone_book.add("Kim", office="1234567", email="kim@company.com")
    phone_book.add("Park", mobile="010-1234-5678", office="2345678")
    phone_book.add("Lee", mobile="010-9876-5432", email="lee@company.com")

    print(phone_book)


if __name__ == "__main__":
    test_prob7()