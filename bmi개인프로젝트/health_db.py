import json
import csv
import pickle

class HealthDB:
    def __init__(self):
        self.json_file = "health_management_project\\data\\health_data.json"
        self.csv_file = "health_management_project\\data\\health_data.csv"
        self.txt_file = "health_management_project\\data\\health_data.txt"
        self.pkl_file = "health_management_project\\data\\health_data.pkl"
        
    def load_data(self):
        with open(self.json_file, "r", encoding="utf-8") as jf:
            jsdata = json.load(jf)
        
        with open(self.csv_file, "r", encoding="utf-8") as cf:
            csvdata = list(csv.DictReader(cf))

        with open(self.txt_file, "r", encoding="utf-8") as tf:
            txtdata = [line.strip().split(",") for line in tf.readlines()]

        with open(self.pkl_file, "rb") as pf:
            pkldata = pickle.load(pf)

        return jsdata, csvdata, txtdata, pkldata

    def save_data(self, jsdata, csvdata, txtdata, pkldata):
        with open(self.json_file, "w", encoding="utf-8") as jf:
            json.dump(jsdata, jf, ensure_ascii=False, indent=4)

        with open(self.csv_file, "w", encoding="utf-8", newline="") as cf:
            writer = csv.DictWriter(cf, fieldnames=csvdata[0].keys())
            writer.writeheader()
            writer.writerows(csvdata)

        with open(self.txt_file, "w", encoding="utf-8") as tf:
            for row in txtdata:
                tf.write(",".join(row) + "\n")

        with open(self.pkl_file, "wb") as pf:
            pickle.dump(pkldata, pf)

#AI 사용
if __name__ == "__main__":
    # 1. 테스트용 원본 데이터 (딕셔너리 리스트)
    records = [
        {"id_num": "H001", "name": "김철수", "birth_year": 2002, "gender": "남", "height": 175.0, "weight": 70.0, "bmi": 22.86, "obesity_status": "정상"},
        {"id_num": "H002", "name": "이영희", "birth_year": 2004, "gender": "여", "height": 162.5, "weight": 54.0, "bmi": 20.44, "obesity_status": "정상"}
    ]

    print("원본 데이터:", records)
    db = HealthDB() # 이미 구현된 클래스

    # 2. TXT 저장을 위한 문자열 리스트 변환 (for 축약문법 활용)
    txt_rows = [
        [r["id_num"], r["name"], str(r["birth_year"]), r["gender"], str(r["height"]), str(r["weight"]), str(r["bmi"]), r["obesity_status"]]
        for r in records
    ]

    # 3. 저장 및 로드 검증
    db.save_data(records, records, txt_rows, records)
    jsdata, csvdata, txtdata, pkldata = db.load_data()

    # 4. CSV에서 문자열로 읽은 숫자/수치형 데이터 복원
    for row in csvdata:
        row["birth_year"] = int(row["birth_year"])
        row["height"] = float(row["height"])
        row["weight"] = float(row["weight"])
        row["bmi"] = float(row["bmi"])

    # 5. TXT에서 읽은 리스트를 원본과 같은 딕셔너리로 복원
    txtdata = [
        {
            "id_num": row[0],
            "name": row[1],
            "birth_year": int(row[2]),
            "gender": row[3],
            "height": float(row[4]),
            "weight": float(row[5]),
            "bmi": float(row[6]),
            "obesity_status": row[7]
        }
        for row in txtdata
    ]

    # 6. 포맷별 결과 비교 출력
    results = {
        "JSON": jsdata,
        "CSV": csvdata,
        "TXT": txtdata,
        "PKL": pkldata
    }

    for file_type, loaded in results.items():
        print(f"\n{file_type}에서 읽은 데이터:", loaded)
        print("원본과 일치:", records == loaded)