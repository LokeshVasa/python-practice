# print(f"{(4/3)*3.14*(float(input())**3):.2f}" )


import pyautogui

import time

# Give yourself a few seconds to switch to the target application
time.sleep(5)

# The text you want to type

for i in range(10):
    text_to_type = '''Gandu'''
    pyautogui.typewrite(text_to_type, interval=0.1) 
    pyautogui.press('enter')


# D:\python-practice\streamlit\app.py