import random
from dict import dict

while True:
  a = random.randint(0,13)
  score = 0
  print(list(dict.keys())[a])

  user_input = input("Translate this into english: ")
  try:
    if user_input == list(dict.values())[a]:
      score = score + 1
      print("That is correct. You gain " + str(score) +" point")
    if user_input == "score":
      print("Your score: " + str(score))
    if user_input != list(dict.values())[a]:
      print("Wrong, the correct word was:" + str(list(dict.values())[a]))
      score = score - 2
      print("Your new score is:" + str(score))

  except:
    print("error")
    exit()
