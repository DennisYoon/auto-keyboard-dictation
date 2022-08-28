from tkinter import *

initSize = {
  "x": 700,
  "y": 450
}

infoText = """아래 입력창에 문자열을 입력하시오.
당신이 입력한 문자열이 pyautogui.write 함수를 이용해 당신이 원하는 어느 입력창에서든 입력될 것입니다.
특히 복사 붙여넣기를 지원하지 않거나 막은 입력창에서 더욱 유용합니다."""

def doAutoKeyboardDictation():
  value = scan.get("1.0", "end-1c")
  print(value)

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

button = Button(
  window,
  text = "실행",
  overrelief = "solid",
  width = 15,
  command = doAutoKeyboardDictation
)

title.pack()
info.pack()
scan.pack()
button.pack(side = "right")

window.mainloop()