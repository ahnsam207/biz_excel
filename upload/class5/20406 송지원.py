# Imports go at the top
from microbit import *

# 초기 시간 설정
current_hour = 0
current_minute = 0
alarm_hour = 14  # 알람 시간 (14시)
alarm_minute = 30  # 알람 분 (30분)

def show_time():
    display.scroll("{:02}:{:02}".format(current_hour, current_minute))

def check_alarm():
    return current_hour == alarm_hour and current_minute == alarm_minute

def main():
    global current_hour, current_minute
    alarm_active = True

    while True:
        if button_a.is_pressed():  # 시간 설정 모드
            display.scroll("Set Hour")
            while button_a.is_pressed():
                pass
            while True:
                current_hour = (current_hour + 1) % 24
                display.scroll("Hour: {}".format(current_hour))
                sleep(1000)
                if button_a.is_pressed():
                    break
        
        if button_b.is_pressed():  # 분 설정 모드
            display.scroll("Set Minute")
            while button_b.is_pressed():
                pass
            while True:
                current_minute = (current_minute + 1) % 60
                display.scroll("Minute: {}".format(current_minute))
                sleep(1000)
                if button_b.is_pressed():
                    break
        
        show_time()  # 현재 시간 표시
        sleep(10000)  # 10초마다 업데이트

        if alarm_active and check_alarm():
            display.show(Image.SAD)
            sleep(2000)
            display.scroll("Alarm! Press A to turn off.")
            
            while True:
                if button_a.is_pressed():
                    alarm_active = False
                    display.clear()
                    break

main()
