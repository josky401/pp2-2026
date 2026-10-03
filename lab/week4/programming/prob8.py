# 파일명: week4/programming/prob8.py
# 작성자: 조하늘
# 작성일: 2026-10-03
# 문제: Song (printSong) 클래스 구현 (파이썬 익스프레스 08번)
# 설계:
#   - Song 클래스: lyrics (가사 리스트) 속성
#   - 메서드: __init__(lyrics_list), sing()
#   - test_prob8(): 리스트 형태의 가사를 전달받아 한 줄씩 출력 검증

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing(self):
        for line in self.lyrics:
            print(line)

def test_prob8():
    aSong = Song([
        "TWINKLE, twinkle, little star",
        "How I wonder what you are!",
        "Up above the world so high,",
        "Like a diamond in the sky."
    ])

    aSong.sing()


if __name__ == "__main__":
    test_prob8()