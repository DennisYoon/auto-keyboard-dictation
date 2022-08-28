from tkinter import *
from akd import doAutoKeyboardDictation

initSize = {
  "x": 700,
  "y": 530
}

infoText = """아래 입력창에 문자열을 입력하시오.
당신이 입력한 문자열이 pyautogui.write 함수를 이용해 당신이 원하는 어느 입력창에서든 입력될 것입니다.
특히 복사 붙여넣기를 지원하지 않거나 막은 입력창에서 더욱 유용합니다.

주의!!! >> 입력창의 키보드 입력은 '영어' 모드로 되어있어야 합니다!!"""

window = Tk()

window.title("auto keyboard dictation")
window.geometry("{}x{}".format(initSize["x"], initSize["y"]))
window.resizable(False, False)

title = Label(
  window,
  text = "Auto Keyboard Dictation",
  width = initSize["x"],
  anchor = "w",
  font = ("", 20)
)

info = Label(
  window,
  text = infoText,
  width = initSize["x"],
  anchor = "w",
  justify = "left"
)

scan = Text(
  window,
  width = 55,
  height = 14,
  font = ("", 17)
)

secAfter = Label(
  window,
  text = "몇 초후 실행??",
  width = initSize["x"],
  anchor = "w"
)

slice = Scale(
  window,
  from_ = 1,
  to = 10,
  length = initSize["x"],
  orient = HORIZONTAL
)

button = Button(
  window,
  text = "실행",
  overrelief = "solid",
  width = 10,
  command = lambda: doAutoKeyboardDictation(scan, slice)
)

title.pack()
info.pack()
scan.pack()
secAfter.pack()
slice.pack()
button.pack(side = "right")

window.mainloop()