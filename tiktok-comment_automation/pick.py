import pyautogui

# Melacak lokasi pointer mouse
currentMouseX, currentMouseY = pyautogui.position()

print(str(currentMouseX) + "," + str(currentMouseY))
