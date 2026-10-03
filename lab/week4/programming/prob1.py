# 파일명: week4/programming/prob1.py
# 작성자: 조하늘
# 작성일: 2026-10-03
# 문제: Cat 클래스 정의 (파이썬 익스프레스 01번)
# 설계:
#   - Cat 클래스: name, age 속성[cite: 3]
#   - 메서드: __init__, __str__, setName, getName, sertAge, getAge
#   - test_prob1(): 인스턴스 생성 및 출력 결과 검증[cite: 3]

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age

    def __str__(self):
        return f"{self.name} {self.age}"


def test_prob1():
    missy = Cat('Missy', 3)
    lucky = Cat('Lucky', 5)

    print(missy)
    print(lucky)


if __name__ == "__main__":
    test_prob1()