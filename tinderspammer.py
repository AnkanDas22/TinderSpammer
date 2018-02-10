import webbrowser
import pyautogui
import time

webbrowser.open('https://www.tinder.com')
input("Press Enter once you're done logging into Tinder")
x=int(input('How many people are you targeting to swipe?\n'))
a=int(input('Right swipe all? - 1\nLeft swipe all? - 2\n'))
print('Click on Tinder screen within 5 seconds')
time.sleep(5)
i=0
while i<x:
    if a==1:
        pyautogui.press('right')
    elif a==2:
        pyautogui.press('left')
    else:
        print('Even Gaben can type till 2')
        break
    i=i+1
    time.sleep(1)
    print('Person',i,'right' if a==1 else 'left','swiped')
