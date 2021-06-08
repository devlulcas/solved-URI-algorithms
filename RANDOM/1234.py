#URI 1234 - DANCING SENTENCE
while True:
  try:
    str = input() 
    case = 1 
    result = ""
    for letter in str:
      if (letter!=" "):
        if case:
          result+=letter.upper()
          case=0
          continue
        result+=letter.lower()
        case=1
        continue
      result+=" "
    print(result)
  except EOFError:
    break