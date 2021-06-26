import pyautogui 
from threading import Thread
import time


def auto_click():
	while True:
		pyautogui.click(button="left")
		time.sleep(0.01)
		pyautogui.click(button="left")
		global stop_threads
		if stop_threads:
			break
        	


def join():
	print("Start Join")
	pyautogui.click(button="right")

	time.sleep(0.3)

	print("skyblock")
	skyblock_x, skyblock_y = pyautogui.locateCenterOnScreen("skyblock.png")
	print(skyblock_x, skyblock_y)
	pyautogui.click(skyblock_x, skyblock_y)

	time.sleep(0.3)

	print("skyb")
	skyb_x, skyb_y = pyautogui.locateCenterOnScreen("skyb.png")
	print(skyb_x, skyb_y)
	pyautogui.click(skyb_x +20, skyb_y+20)
	time.sleep(1)
def restart():
	print("Starting restart")
	while True:
		cris = pyautogui.locateCenterOnScreen("sword.png")
		if not cris:
			print("Join")
			time.sleep(120)
			join()
		else:
			print("Auto click")
			pyautogui.click(button="left")
			
		

if __name__ == '__main__':
	print("Start...")
	time.sleep(2)
	restart()