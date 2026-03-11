import datetime
from zoneinfo import ZoneInfo # Python 3.9+ 內建

# 直接指定台北時區
now_tw = datetime.datetime.now(ZoneInfo("Asia/Taipei"))

print("台灣時間：", now_tw.hour, "點", now_tw.minute, "分")
