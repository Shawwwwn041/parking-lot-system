import datetime
from zoneinfo import ZoneInfo # Python 3.9+ 內建
def get_timing():
    start_time = datetime.datetime.now(ZoneInfo("Asia/Taipei"))
    print("台灣時間：", start_time.hour, "點", start_time.minute, "分")
