
import threading
from time import sleep
from PIL import Image, ImageGrab
from pytesseract import pytesseract
from pynput.keyboard import Key, Controller
keyboard = Controller()
sometexts = ["Me-wow, is that the latest Felinor fashion?",
"So, what's keeping you busy these days?",
"Hey Hivekin, can I bug you for a moment?",
"So, how's work?",
"Wow, this breeze is great, right?",
"Sometimes I have really deep thoughts about life and stuff.",
"Some weather we're having, huh?",
"You ever been to a Canor restaurant? The food's pretty howlright."]

find = ["Felinor fashion?",
"keeping you busy these",
"bug you for a moment",
"So, how's work?",
"this breeze is great",
"have really deep thoughts",
"Some weather",
"Canor restaurant"]

import pyautogui

path_to_tesseract = r"C:\Users\Owl\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = path_to_tesseract

def checker(v):
  count = -1
  for i in find:
   count = count+1
   if v != "" and v.lower().find(i.lower()) != -1:
    print(v.lower(),i.lower())
    #pyautogui.press('/')
    pyautogui.typewrite(sometexts[count])
    keyboard.press(Key.enter)
    sleep(.11)
    pyautogui.click(50, 100)

while True:
 snapshot = ImageGrab.grab()
 text = pytesseract.image_to_string(snapshot)
 for v in text[:-1].split("\n"):
  checker(v)
  #processThread = threading.Thread(target=checker, args=[v])  # <- 1 element list
  #processThread.start()
