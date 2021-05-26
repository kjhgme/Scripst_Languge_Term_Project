import time
import datetime

t = time.time()
today = int(time.strftime("%Y%m%d", time.localtime(t)))
hour = int(time.strftime('%H', time.localtime(time.time())))

print(type(today))
print(today)