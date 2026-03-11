from datetime import datetime #時間模組
from zoneinfo import ZoneInfo 
def get_timing():
    now_time = datetime.now(ZoneInfo("Asia/Taipei"))
    #print("台灣時間：", now_time.hour, "點", now_time.minute, "分")
    return now_time 


