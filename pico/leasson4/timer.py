from machine import Timer

def hello(t):
    print(time.freq)
    
tim = Timer(period=5000, mode=Timer.ONE_SHOT, callback=lambda t:print(1))
tim.init(period=2000, mode=Timer.PERIODIC, callback=hello)


