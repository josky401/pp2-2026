import json
import os

class HealthDatabase:
    def __init__(self, filename="health_data.json"):
        self.filename = filename
        self.records = []  # 환자 기록을 담을 리스트
        self.load_data()   # 시작할 때 파일에서 데이터 불러오기

    def add_record(self, name, age, height, weight):
        # BMI 계산 (키는 cm이므로 m로 변환)
        height_m = height / 100
        bmi = round(weight / (height_m ** 2), 2) if height > 0 else 0
        
        # 간단한 비만도 상태 판정
        if bmi < 18.5:
            status = "저체중"
        elif bmi < 23:
            status = "정상"
        elif bmi < 25:
            status = "과체중"
        else:
            status = "비만"

        # 데이터 딕셔너리 생성
        record = {
            "name": name,
            "age": age,
            "height": height,
            "weight": weight,
            "bmi": bmi,
            "status": status
        }
        
        self.records.append(record)
        self.save_data()

    def save_data(self):
        #현재 데이터 목록을 JSON 파일로 안전하게 저장합니다.
        try:
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump(self.records, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"[경고] 파일 저장 실패: {e}")

    def load_data(self):
        #프로그램 실행 시 파일에서 데이터를 불러옵니다. (파일이 없으면 빈 리스트)
        if not os.path.exists(self.filename):
            self.records = []
            return

        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                self.records = json.load(f)
        except Exception as e:
            print(f"[경고] 파일이 손상되었거나 읽을 수 없습니다: {e}")
            self.records = []