import pyautogui
import time


class MouseControl():
    def __init__(self, mouse_pos_x=0, mouse_pos_y=0):
        self.mouse_pos_x = mouse_pos_x
        self.mouse_pos_y = mouse_pos_y

    def get_mouse_pos(self):
        currentMouseX, currentMouseY = pyautogui.position()
        return [currentMouseX, currentMouseY]
    def move_mouse_to(self, mouse_pos_x, mouse_pos_y):
        pyautogui.moveTo(mouse_pos_x, mouse_pos_y)


# screenWidth, screenHeight = pyautogui.size()
# print(f"Screen width is: {screenWidth}, screen height is: {screenHeight}")
#
# currentMouseX, currentMouseY = pyautogui.position()
# print(f"Mouse x is: {currentMouseX}, mouse y is: {currentMouseY}")
#
# # while True:
# #     currentMouseX, currentMouseY = pyautogui.position()
# #     print(f"Mouse x is: {currentMouseX}, mouse y is: {currentMouseY}")
# #     time.sleep(1)
#
# time.sleep(2)
# pyautogui.moveTo(70, 900)

mouse_controller = MouseControl()
list = mouse_controller.get_mouse_pos()
print(list)