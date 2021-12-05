import pyautogui 
import time

def press(but):
	pyautogui.keyDown(but)
	time.sleep(0.01)
	pyautogui.keyUp(but)


def join():
	print("Start Join")
	press("H")
	time.sleep(5)
	press("1")

	pyautogui.click(button="right")

	time.sleep(0.3)

	print("skyblock")
	try:
		skyblock_x, skyblock_y = pyautogui.locateCenterOnScreen("skyblock1.png")
		print(skyblock_x, skyblock_y)
		pyautogui.moveTo(skyblock_x, skyblock_y)
		pyautogui.click()
	except:
		print("except")
		skyblock_x, skyblock_y = pyautogui.locateCenterOnScreen("skyblock.png")
		print(skyblock_x, skyblock_y)
		pyautogui.moveTo(skyblock_x, skyblock_y)
		pyautogui.click()
	time.sleep(0.3)

	print("zeldrix")
	skyb_x, skyb_y = pyautogui.locateCenterOnScreen("zeldrix.png")
	print(skyb_x, skyb_y)
	pyautogui.moveTo(skyb_x , skyb_y + 25)
	pyautogui.click()
	time.sleep(10)
def restart():
	x=0
	print("Starting restart")
	while True:
		cris = pyautogui.locateCenterOnScreen("picaxe.png")
		if not cris:
			pyautogui.mouseUp(button=pyautogui.LEFT)
			print("Join")
			time.sleep(10)
			join()
		else:
			x+=1
			print("Auto click")
			pyautogui.mouseDown(button=pyautogui.LEFT)
			press(str(x))
			print(x)
			if x == 9:
				x =0
				# print(x)

if __name__ == '__main__':
	print("Start...")
	time.sleep(7)
	restart()