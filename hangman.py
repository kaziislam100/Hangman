# Import random integer from the function import
from random import randint

# prints a welcome message with your name
name = input("What is your name?")
print(name+"," " Welcome to Hangman. A word will be chosen at random and",
               "you must try to guess the word correctly letter by letter",
               "before you run out of attempts. Good luck!"
               )

# These are the list of the words
words = ["pie is good", "tiger", "cactus", "biology", "tornado", "modem", "pollution", "addidas", "hangman", "soccer"]
hints = ["It is the name of a food",
         "It is an animal",
         "It is a plant",
         "It is a subject in school",
         "It is realted to the earth's atmosphere",
         "It is related to the internet",
         "It is realted to the environment",
         "It is related to a sporting goods company",
         "It is the name of a game",
         "It is the name of a very popular sport"]

# This selects a word at random
selected_word = words[randint(0,len(words)-1)]

# This prints underscores for the number of letters in the selected word
underscores = []
for i in range(len(selected_word)):
  underscores.append("_")

# This puts the length of the selected word in the answer
answer = []
for i in range(len(selected_word)):
    answer.append(selected_word[i])

# This prints out the hints with the corresponding word
if (selected_word == words[0]):
    print("Hint:", hints[0])
elif (selected_word == words[1]):
    print("Hint:", hints[1])
elif (selected_word == words[2]):
    print("Hint:", hints[2])
elif (selected_word == words[3]):
    print("Hint:", hints[3])
elif (selected_word == words[4]):
    print("Hint:", hints[4])
elif (selected_word == words[5]):
    print("Hint:", hints[5])
elif (selected_word == words[6]):
    print("Hint:", hints[6])
elif (selected_word == words[7]):
    print("Hint:", hints[7])
elif (selected_word == words[8]):
    print("Hint:", hints[8])
elif (selected_word == words[9]):
    print("Hint:", hints[9])
elif (selected_word == words[10]):
    print("Hint:", hints[10])

# Empty list to place what letters were guessed
guessed = []

# This checks the condition and runs the while loop and displays the underscores
correct = 0
game = True
while(game == True):
  display = ""
  for i in underscores:
      display += i + " "
  print(display)

# This asks for the user's input and checks to see if it matches with one of the letters
# If it does it replaces the corresponding underscore and the letter and print out how many
# Of the correct letters you got and also what letters
  user_input = input("Enter a letter: ")

  for i in range(len(selected_word)):
      if (user_input != display):
          guessed.append(user_input)
  print(guessed)
  for i in range(len(selected_word)):
      if(user_input == selected_word[i]):
          underscores[i] = user_input
          correct = correct + 1
  print("You got", correct, "correct letters out of", len(selected_word))

# When the user gets everything right it ends the loop and prints a congratualtion message with the selected word
  if (underscores == answer):
      game = False
      print("Congratulations, You Figured Out The Hidden Word: ",
            selected_word)
      break
