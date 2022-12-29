class FlashCard:

  def __init__(self):
    self.__fruits = {
        'apple':'red',
        'banana':'yellow',
        'guava':'green',
        'watermelon':'pink'
    }

  def quiz(self):
    import random

    while True:
      fruit,color = random.choices(list(self.__fruits.items()))[0]
      print(f"what is the color of {fruit}")

      user_answer = input()

      if user_answer.lower() == color:
        print("Correct")

      else:
        print("Incorrect")        

      option = int(input("Enter 1 to play again & 0 to exit"))

      if option == 0:
        break