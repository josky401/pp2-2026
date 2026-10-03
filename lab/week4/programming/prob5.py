# 파일명: week4/programming/prob5.py
# 작성자: 조하늘
# 작성일: 2026-10-03
# 문제: Triangle 클래스 구현 (파이썬 익스프레스 05번)
# 설계:
#   - Triangle 클래스: angle1~3, numberOfSides=3 속성
#   - 메서드: __init__, __str__, get/setAngle, checkAngles
#   - test_prob5(): 객체 생성 및 checkAngles 동작 검증

class Triangle:
    def __init__(self, a1, a2, a3, numberOfSides = 3):
        self.angle1 = a1
        self.angle2 = a2
        self.angle3 = a3
        self.numberOfSides = numberOfSides

    def getAngle1(self):
        return self.angle1

    def setAngle1(self, value):
        self.angle1 = value

    def getAngle2(self):
        return self.angle2

    def setAngle2(self, value):
        self.angle2 = value

    def getAngle3(self):
        return self.angle3

    def setAngle3(self, value):
        self.angle3 = value

    def checkAngles(self):
        """내각의 합이 180도인지 확인"""
        return (self.angle1 + self.angle2 + self.angle3) == 180

    def __str__(self):
        return f"Triangle({self.angle1}, {self.angle2}, {self.angle3})"


def test_prob5():
    triangle = Triangle(90, 30, 60)
    print(triangle.checkAngles())  # True


if __name__ == "__main__":
    test_prob5()