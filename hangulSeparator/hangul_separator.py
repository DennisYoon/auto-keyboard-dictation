from hangulSeparator._initial_middle_final import *
from hangulSeparator._exceptions import exceptions

def _separate(letter):
  hangulStart = 44032
  unicodeOfWord = ord(letter)

  if letter in exceptions:
    return {
      "EN": letter
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

if __name__ == "__main__":
  ex = separate("hello world")
  print(ex)