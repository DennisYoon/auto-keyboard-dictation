from time import sleep
from pyautogui import press, write
import pyautogui as py
from src.separator import separate

kr2en = {
  'ㅂ': 'q', 'ㅈ': 'w', 'ㄷ': 'e', 'ㄱ': 'r', 'ㅅ': 't', 'ㅛ': 'y', 'ㅕ': 'u', 'ㅑ': 'i', 'ㅐ': 'o', 'ㅔ': 'p',
  'ㅁ': 'a', 'ㄴ': 's', 'ㅇ': 'd', 'ㄹ': 'f', 'ㅎ': 'g', 'ㅗ': 'h', 'ㅓ': 'j', 'ㅏ': 'k', 'ㅣ': 'l',
  'ㅋ': 'z', 'ㅌ': 'x', 'ㅊ': 'c', 'ㅍ': 'v', 'ㅠ': 'b', 'ㅜ': 'n', 'ㅡ': 'm',
  'ㅃ': 'Q', 'ㅉ': 'W', 'ㄸ': 'E', 'ㄲ': 'R', 'ㅆ': 'T', 'ㅒ': 'O', 'ㅖ': 'P'
}

def doAutoKeyboardDictation(scan, slice):
  value = toEnglish(scan.get("1.0", "end-1c"))
  wait = slice.get()
  sleep(wait)
  dictate(value)

def toEnglish(value):
  separated = separate(value)
  result = []
  for v in separated:
    if "KR" in v:
      krResult = ""
      for word in v["KR"]:
        krResult += kr2en[word]
      result.append({"KR": krResult})
    if "EN" in v:
      result.append({"EN": v["EN"]})
  return result

def dictate(value):
  py.PAUSE = 0
  nowMode = "E"
  for v in value:
    if "KR" in v:
      if nowMode == "E":
        press("hangul")
        nowMode = "K"
      write(v["KR"])
    elif "EN" in v:
      if nowMode == "K":
        press("hangul")
        nowMode = "E"
      write(v["EN"])