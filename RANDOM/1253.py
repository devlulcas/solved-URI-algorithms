#URI 1253 - CAESAR CIPHER
from string import ascii_uppercase
n = int(input())
alphabet = ascii_uppercase

for i in range(n):
  phrase = input()
  pswd = int(input())
  decoded = ""
  for str in phrase:
    a = alphabet.index(str) - pswd
    decoded += alphabet[a]
  print(decoded)