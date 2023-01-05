exceptions = [
  "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
  "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
  "`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=", "\\", "[", "]", ";", "\"", ",", ".", "/",
  "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "|", "{", "}", ":", "\'", "<", ">", "?", " ", "\n", "  "
]
initials = [
  "ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ",
  "ㅂ", "ㅃ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ",
  "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"
]

middles = [
  "ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ",
  "ㅖ", "ㅗ", "ㅗㅏ", "ㅗㅐ", "ㅗㅣ", "ㅛ", "ㅜ",
  "ㅜㅓ", "ㅜㅔ", "ㅜㅣ", "ㅠ", "ㅡ", "ㅡㅣ", "ㅣ"
]

finals = [
  "", "ㄱ", "ㄲ", "ㄱㅅ", "ㄴ", "ㄴㅈ", "ㄴㅎ",
  "ㄷ", "ㄹ", "ㄹㄱ", "ㄹㅁ", "ㄹㅂ", "ㄹㅅ", "ㄹㅌ",
  "ㄹㅍ", "ㄹㅎ", "ㅁ", "ㅂ", "ㅂㅅ", "ㅅ", "ㅆ",
  "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"
]

def _separate(letter):
  hangulStart = 44032
  unicodeOfWord = ord(letter)

  if letter in exceptions:
    return {
      "EN": letter
    }
  else:
    if exception(letter):
      return {
        "KR": letter
      }
    else:
      relativeSize = unicodeOfWord - hangulStart

      initialIDX = int(relativeSize / 588)
      middleIDX = int((relativeSize - (initialIDX * 588)) / 28)
      finalIDX = int(relativeSize % 28)

      return {
        "KR": initials[initialIDX] + middles[middleIDX] + finals[finalIDX]
      }

def separate(word):
  result = []
  for letter in word:
    value = _separate(letter)
    result.append(value)
  
  return result

def exception(letter):
  exceptions = "ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎㅏㅑㅓㅕㅗㅛㅜㅠㅡㅣㄲㄸㅃㅆㅉㄳㄵㄶㄺㄻㄼㄽㄾㄿㅀㅄㅐㅒㅔㅖㅘㅙㅚㅝㅞㅟㅢ"
  if letter in exceptions:
    return True
  return False