#main.py
import car_module as c
import datime_test
parking_records ={} #紀錄停車場車輛車牌
print("======== 停車場系統 2.0 啟動中 ========")
# 原本的 while True:
while True:
    guest = input("請問要進場'enter'還是離場'exit'？").lower()
    if guest =='enter':
        cars_in = input("請輸入車牌號碼: ").upper()
        if c.car_module(cars_in):
            parking_records[cars_in] = datime_test.get_timing()
            print(f"{cars_in}，歡迎！已記錄時間")
        else:
            print("格式辨識失敗，請重新輸入。")
    elif guest =='exit':
        print(f"【系統提示】目前場內車輛：{list(parking_records.keys())}")
        cars_out = input("請輸入車牌號碼").upper().strip()
        if cars_out in parking_records:
            exit_time = datime_test.get_timing()
            #抓取現在離場時間
            entry_time = parking_records[cars_out]
            total_timing = round((exit_time - entry_time).total_seconds())/60
            print(f"你所停的總時數：{total_timing}")
            del parking_records[cars_out]
        else:
           print(f"找不到車牌 '{cars_out}'，請確認是否與進場時輸入一致！")

            