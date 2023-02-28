import pyautogui as pg
import time

print("Program will run after 20 seconds")
time.sleep(20)

print("Running")

for i in range(100):
    pg.write("I love You")
    time.sleep(0.1)
    pg.press("Enter")
    
print("DONE!!!!")

