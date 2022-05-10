import os
import time
import sys
import pyautogui
day = time.asctime()
currentTime = day[11:13]+day[14:16]
day = day[:3]
print(day)
print(currentTime)
dayTime = ("Mon", "Wed", "Fri")
startTime = ("1000", "0830", "0700")
while True:
    executionTime = None
    if day in dayTime:
        if day == dayTime[0]:
            executionTime = startTime[0]
        elif day == dayTime[1]:
            executionTime = startTime[1]
        elif day == dayTime[2]:
            executionTime = startTime[2]

        if executionTime in startTime:
            chromeLocation = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            ccnaClassLink = "https://meet.google.com/bdf-ieas-eqf?pli=1&authuser=2"
            navBarLocation = (340, 51)
            mikeLocation = (724, 720)
            cameraLocation = (784, 728)
            joinLocation = (1242, 594)
            os.startfile(chromeLocation)
            time.sleep(3)
            pyautogui.moveTo(navBarLocation[0], navBarLocation[1], 5)
            pyautogui.click()
            pyautogui.write(ccnaClassLink)
            pyautogui.press('enter')
            pyautogui.moveTo(mikeLocation[0], mikeLocation[1], 5)
            pyautogui.click()
            pyautogui.moveTo(cameraLocation[0], cameraLocation[1], 2)
            pyautogui.click()
            pyautogui.moveTo(joinLocation[0], joinLocation[1], 2)
            pyautogui.click()
            input()
        else:
            time.sleep(180)

    else:
        print("Exiting the code.")
        sys.exit()
