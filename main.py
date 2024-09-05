from startingPc import start_pc, setSoundMax
from soundChanger import soundChanger
from lockScreen import lock_screen
from ctr_c import ctrlRand
import threading
import time
import keyboard
import os

stop_flag = threading.Event()

def lock_screenMain():
    while True:
        time.sleep(1699)
        lock_screen()

def ctrlRandMain():
    while True:
        ctrlRand()

def start_pcMain():
    start_pc()

def soundChangerMain():
    while True:
        time.sleep(120)
        soundChanger()

def stop_program():
    stop_flag.set()
    os._exit(0)

def keyboard_listener():
    keyboard.add_hotkey('a+b+c+d', stop_program)

def statusUpdateMain():
    soundChanger_interval = 300
    lock_screen_interval = 1699
    soundChanger_time_left = soundChanger_interval
    lock_screen_time_left = lock_screen_interval

    while True:
        time.sleep(5)
        soundChanger_time_left -= 5
        lock_screen_time_left -= 5

        if soundChanger_time_left <= 0:
            soundChanger_time_left = soundChanger_interval

        if lock_screen_time_left <= 0:
            lock_screen_time_left = lock_screen_interval

        print(f"Time until soundChanger: {soundChanger_time_left} seconds")
        print(f"Time until lock_screen: {lock_screen_time_left} seconds")

def everythingRunning():
    start_pcMain()
    
    thread1 = threading.Thread(target=ctrlRandMain)
    thread2 = threading.Thread(target=soundChangerMain)
    thread3 = threading.Thread(target=lock_screenMain)
    thread4 = threading.Thread(target=statusUpdateMain)
    thread5 = threading.Thread(target=keyboard_listener)

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()

if __name__ == '__main__':
    everythingRunning()