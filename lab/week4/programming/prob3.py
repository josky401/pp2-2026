# 파일명: week4/programming/prob3.py
# 작성자: 조하늘
# 작성일: 2026-10-03
# 문제: Box 클래스 구현 (파이썬 익스프레스 03번)
# 설계:
#   - Box 클래스: length, height, depth 속성
#   - 메서드: __init__, __str__, get/set (Length, Height, Depth)
#   - test_prob3(): Box 객체 생성, 정보 및 부피 계산 출력 검증

class Box:
    def __init__(self, l, h, d):
        self.length = l
        self.height = h
        self.depth = d

    def getLength(self):
        return self.length

    def setLength(self, length):
        self.length = length

    def getHeight(self):
        return self.height

    def setHeight(self, height):
        self.height = height

    def getDepth(self):
        return self.depth

    def setDepth(self, depth):
        self.depth = depth

    def __str__(self):
        return f"({self.length}, {self.height}, {self.depth})"


def test_prob3():
    b1 = Box(100, 100, 100)
    print(b1)
    print("상자의 부피는", b1.getHeight() * b1.getLength() * b1.getDepth())


if __name__ == "__main__":
    test_prob3()