# bmi.py in week2
# bmi 계산 함수
# Body Mass Index (BmI) 계산 함수
#

def get_bmi(weight_kg:float, height_cm:float) -> float:
    bmi = weight_kg / (height_cm/100) ** 2
    return bmi

def test_get_bmi():
    height_cm = 170
    weight_kg = 70
    b = get_bmi(weight_kg, height_cm)
    print(f"키({height_cm}) 몸무게({weight_kg}) BMI는 {b}입니다")

if __name__ == "__main__":
    test_get_bmi()