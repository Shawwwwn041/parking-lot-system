#main.py
import car_module as c
while True:
    cars_in = input("請輸入車牌號碼: ").upper()
    if c.car_module(cars_in):
        print("車牌格式正確！")
        break
else:
    print("格式辨識失敗，請重新輸入。")