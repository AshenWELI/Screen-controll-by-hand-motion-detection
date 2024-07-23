import pyautogui

def move_mouse(x, y, width, height):
    screen_width, screen_height = pyautogui.size()
    x = int(x * screen_width / width)
    y = int(y * screen_height / height)
    pyautogui.moveTo(x, y)