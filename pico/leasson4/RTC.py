from machine import RTC

#取得目前日期
rtc = RTC()
dt = rtc.datetime()
print(dt)

#重設日期
rtc.datetime((2017,8,23,2,12,48,0,0))
print(dt)

# 格式化日期時間為 yyyy-MM-dd HH:mm:ss
formatted_datetime = "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(
    dt[0], dt[1], dt[2], dt[4], dt[5], dt[6]
)

print(formatted_datetime)