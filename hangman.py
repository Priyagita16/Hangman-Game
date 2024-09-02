import random

def word_selection(ch):
  #Selects a random word from a list from the category chosen by the player.
  if ch==1:
      word_list=["elephant","kangaroo","penguin","crocodile","monkey","giraffe","rabbit","mouse","chicken","parrot","lizard","donkey","chipmunk","tiger","cheetah","flamingo","hummingbird","tortoise","chameleon","peacock","octopus","jellyfish","whale","shark"]
  elif ch==2:
      word_list=["banana","orange","grapes","strawberry","mango","watermelon","pineapple","potato","tomato","cucumber","cheese","sandwich","noodles","ice cream","popcorn","cookies","cupcake","chocolate","pudding","waffles","pancakes","avocado","jackfruit","biryani"]
  elif ch==3:
      word_list=["canada","mexico","argentina","brazil","england","spain","italy","russia","poland","india","pakistan","norway","sweden","ireland","france","germany","china","japan","thailand","indonesia","malaysia","philippines","egypt","morocco","nigeria","australia"]
  elif ch==4:
      word_list=["titanic","avatar","joker","inception","interstellar","jurassic park","the avengers","the shawshank redemption","harry potter","the matrix","terminator","finidng nemo","final destination","fast and furious","lord of the rings","la la land","black swan","slumdog millionaire","life of pi"]
  elif ch==5:
      word_list=["molecule","kinetic energy","gravity","solar system","photosynthesis","respiration","evolution","organism","genetics","chemical reaction","periodic table","acceleration","electricity","magnetism","motion","velocity","friction","bacteria","chromosome","catalyst","wavelength","frequency"]
  elif ch==6:
      word_list=["computer","laptop","internet","software","hardware","website","network","smartphone","printer","scanner","monitor","keyboard","tablet","router","database","social media","email","processor","motherboard","camera","device","bluetooth","gadget","application","adapter","youtube","hacking","phishing"]
  return random.choice(word_list)

def display_hangman(tries):
  #Displays the hangman based on the number of incorrect guesses.
  stages = ["""
  --------
  |      |
  |
  |
  |
  |
  ========
  """,
  """
  --------
  |      |
  |      O
  |
  |
  |
  ========
  """,
  """
  --------
  |      |
  |      O
  |      |
  |
  |
  ========
  """,
  """
  --------
  |      |
  |      O
  |     /|
  |
  |
  ========
  """,
  """
  --------
  |      |
  |      O
  |     /|\ 
  |
  |
  ========
  """,
  """
  --------
  |      |
  |      O
  |     /|\ 
  |     / 
  |
  ========
  """,
  """
  --------
  |      |
  |      O
  |     /|\ 
  |     / \ 
  |
  ========
  """
  ]
  print(stages[tries])

def display_word(word, guessed):
  #Displays the word with guessed letters and underscores.
  word_with_spaces = list(word)
  word_display = ""
  for i, letter in enumerate(word_with_spaces):
    if letter==" ":
      word_display+="  "
    elif letter in guessed:
      word_display += letter+" "
    else:
      word_display += "_ "
  print(word_display)
  print()

def play_game():
  #Contains the main game logic.
  
  print()
  #displays categories from which the user can choose for the game
  print("CATEGORIES: ")
  print("1. Animals")
  print("2. Food")
  print("3. Countries")
  print("4. Movies")
  print("5. Science")
  print("6. Technology")
  ch=int(input("Select a category (1-6): "))
  print()
  if ch==1:
      print("You have selected ANIMALS!")
  elif ch==2:
      print("You have selected FOOD!")
  elif ch==3:
      print("You have selected COUNTRIES!")
  elif ch==4:
      print("You have selected MOVIES!")
  elif ch==5:
      print("You have selected SCIENCE!")
  elif ch==6:
      print("You have selected TECHNOLOGY!")
  else:
      print("Choose a valid option between 1-6")
  word = word_selection(ch)
  word_without_spaces = word.replace(" ", "")
  word_length = len(word_without_spaces)
  guessed = []
  tries = 0
  
  
  display_hangman(tries)
  result=""
  for i in word:
      if i.isalpha():
          result+="_ "
      else:
          result+="  "
  print(result)
  print()
        
  
  while tries < 6 and set(guessed) != set(word_without_spaces):
    guess = input("Guess a letter: ").lower()
    
    if guess in guessed:
      print("You already guessed that letter!")
      print()
    elif guess not in word_without_spaces:
      print(guess, "is not in the word.")
      tries += 1
      display_hangman(tries)
    else:
      print("Good guess!")
      print()
      guessed.append(guess)
    
    display_word(word, guessed)
    
  if tries == 6:
    print("You lose! The word was", word)
    print()
  else:
    print("You win!")

  #asks the player if they want to play again
  play=input("Do you want to play again? ")
  if play.lower()=="yes":
      print()
      play_game()
  else:
      exit
      
print("Welcome to Hangman!")
#function call to begin the game
play_game()
