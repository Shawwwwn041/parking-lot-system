#停車場系統
import datetime #確認停車時間
car_num = input("車牌號").upper()
num_part = car_num.split("-")
if len(num_part) == 2:
    print(f"切開的結果為{num_part}")
else:
    print("車牌格式不正確！")

