import time  
  
def countdown(t):  
    while t:  
        mins, secs = divmod(t, 60)  
        timer = '{:02d}:{:02d}'.format(mins, secs)  
        print(timer, end="\r")  
        time.sleep(1)  
        t -= 1  
    print('倒计时结束!')  
  
# 测试倒计时函数，从10秒开始倒计时  
countdown(10)
