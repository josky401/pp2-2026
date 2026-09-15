# 문제

# 여러 학생들의 키와 몸무게를 리스트로 입력받아 BMI 리스트를 출력하는
# 함수와 테스트하는 함수를 작성하시오.
# BMI 함수는 지난 시간에 작성한 get_BMI 함수를 이용하여 작성하시오.

def get_BMI(weight, height):
    height = height / 100
    BMI = weight / (height * height)
    return BMI

def test_get_BMI(weight, height):
    bmi = get_BMI(weight, height)
    return bmi

print(test_get_BMI(70, 170))