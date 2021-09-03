#imports
import pyautogui
import time
import keyboard
################################################################
#vars
IsPressed = False
sleep = time.sleep
################################################################
#configs
print("Made By Cody666#5618, v1.0.3")
print("Enter Amount Of Clicks:")
kys = int(input())
sleep(0.1)
print("Enter Keybind")
keyhold = (input())
sleep(0.1)
print("If You Want To Change Any Setting You Have To Restart This Program")
################################################################
#loop function
def here():
    print(r""" _______
/ |0|0| \
|___|___|
|       |
|       |
|       |
|       |
\_______/""")
    print("Mouse Hehe")
################################################################
#main "loop?"
while True:
    if not keyboard.is_pressed(keyhold):
        IsPressed = False
    while not IsPressed:
        sleep(0.05)
        if keyboard.is_pressed(keyhold):
            sleep(0.05)
            here()
            IsPressed = True
            pyautogui.click(None,None,kys)
################################################################        



