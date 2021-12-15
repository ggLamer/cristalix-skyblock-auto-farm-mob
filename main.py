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

	time.sleep(1.3)

	try:
		try:
			print("skyblock1 icon")
			skyblock_x, skyblock_y = pyautogui.locateCenterOnScreen("skyblock1.png")
			print(skyblock_x, skyblock_y)
			pyautogui.moveTo(skyblock_x, skyblock_y)
			pyautogui.click()
		except:
			print("skyblock icon")
			skyblock_x, skyblock_y = pyautogui.locateCenterOnScreen("skyblock.png")
			print(skyblock_x, skyblock_y)
			pyautogui.moveTo(skyblock_x, skyblock_y)
			pyautogui.click()
	except:
		print("skyblock icon no viseble")
		press("esc")
		print("return\n")
		return 
	time.sleep(1)
	try:
		try:
			print("Slot 1")
			skyb_x, skyb_y = pyautogui.locateCenterOnScreen("2slot.png")
			print(skyb_x, skyb_y)
			pyautogui.moveTo(skyb_x + 25, skyb_y + 25)
			pyautogui.click()
		except:
			print("Slot 2")
			skyb_x, skyb_y = pyautogui.locateCenterOnScreen("1slot.png")
			print(skyb_x, skyb_y)
			pyautogui.moveTo(skyb_x , skyb_y + 25)
			pyautogui.click()
	except:
		print("No viseble skyblock server")
		press("esc")
		print("return\n")
		return
	time.sleep(5)

def main():
	while True:
		
		cris = pyautogui.locateCenterOnScreen("picaxe.png")
		if not cris:
			pyautogui.mouseUp(button=pyautogui.LEFT)
			print("Join")
			join()
			
		else:
			print("DOWN LEFT")
			press("1")
			pyautogui.mouseDown(button=pyautogui.LEFT)
		
			

if __name__ == '__main__':
	print("Starting... AFK Mineing")
	time.sleep(5)
	main()