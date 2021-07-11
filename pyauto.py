import pyautogui as pgui
import time

print(pgui.position())

print(pgui.size())

pgui.click()

pgui.click(x=3296,y=10,duration=1)

pgui.screenshot('sample.png')

pgui.screenshot('sample.png',region=(0,200,300,300))

pgui.FAILSAFE = True
