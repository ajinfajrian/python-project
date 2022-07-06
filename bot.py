#!/usr/bin/env python3
import pyautogui
import time, random, signal, sys

word_list = [
        "test 1",
        "test",
        ]
print("CTRL+C for stop the program")
n = 0
while n > -1:
    try:
        pyautogui.click(494,1043) # Klik box comments
        time.sleep(4)
        n += 1
        pyautogui.write(random.choice(word_list)+ " - " + str(n), interval=0.2)
        time.sleep(4)
        pyautogui.click(900,1038) # Klik tombol kirim
        time.sleep(7)
    except KeyboardInterrupt:
        print(" - Running lagi dong")
        sys.exit(0)
