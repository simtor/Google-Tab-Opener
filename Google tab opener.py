import time
import winsound
import subprocess

active = True

def getNumeric(prompt):
    while True:
        response = input(prompt)
        try:
            return int(response)
        except ValueError:
            print("Please only input a number ")

second = getNumeric("Enter number ")


for i in range(second):
    print(str(second - i) + " seconds remaining ")
    time.sleep(1)

print('end')

winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'


for i in range(50):
    for i in range(5*55):
        subprocess.call([chrome_path])
        subprocess.call([chrome_path])
        subprocess.call([chrome_path])
