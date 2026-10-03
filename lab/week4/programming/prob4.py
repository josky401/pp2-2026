# 파일명: week4/programming/prob4.py
# 작성자: 조하늘
# 작성일: 2026-10-03
# 문제: Rectangle 클래스 구현 (파이썬 익스프레스 04번)
# 설계:
#   - Rectangle 클래스: x, y, width, height 속성
#   - 메서드: __init__, __str__, getter/setter, getArea, overlap
#   - test_prob4(): Rectangle 객체 생성 및 overlap 겹침 여부 검증

class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    def getX(self):
        return self.x

    def setX(self, x):
        self.x = x

    def getY(self):
        return self.y

    def setY(self, y):
        self.y = y

    def getWidth(self):
        return self.width

    def setWidth(self, width):
        self.width = width

    def getHeight(self):
        return self.height

    def setHeight(self, height):
        self.height = height

    def getArea(self):
        return self.width * self.height

    def overlap(self, r):
        if self.x + self.width <= r.x or r.x + r.width <= self.x:
            return False
        if self.y + self.height <= r.y or r.y + r.height <= self.y:
            return False
        return True

    def __str__(self):
        return f"Rectangle(x={self.x}, y={self.y}, w={self.width}, h={self.height})"


def test_prob4():
    r1 = Rectangle(0, 0, 100, 100)
    r2 = Rectangle(10, 10, 100, 100)

    if r1.overlap(r2):
        print("r1과 r2는 서로 겹칩니다.")
    else:
        print("r1과 r2는 겹치지 않습니다.")


if __name__ == "__main__":
    test_prob4()