import random


HANGMAN_PICS = [''' 
   +---+
       | 
       | 
       | 
      ===''', ''' 
   +---+ 
   0   | 
       | 
       |
      ===''', ''' 
   +---+ 
   0   | 
   |   | 
       | 
      ===''', ''' 
   +---+ 
   0   | 
  /|   | 
       | 
      ===''', ''' 
   +---+ 
   0   | 
  /|\  | 
       | 
      ===''', ''' 
   +---+ 
   0   | 
  /|\  | 
  /    | 
      ===''', ''' 
   +---+ 
   0   | 
  /|\  | 
  / \  |
      ===''']


words = '''аист акула бабуин баран барсук бобр бык верблюд волк воробей ворон выдра голубь гусь жаба зебра змея 
индюк кит кобра коза козел койот корова кошка кролик крыса курица лама ласка лебедь лев лиса лосось лось 
лягушка медведь моллюск моль мул муравей мышь норка носорог обезьяна овца окунь олень орел осел панда паук питон 
попугай пума семга скунс собака сова тигр тритон тюлень утка форель хорек черепаха ястреб ящерица'''.split()

def getRandomWord(wordList):
    #Эта функция возвращает случайную строку из переданного списка.
    wordIndex = random.randint(0,len(wordList)-1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print("Ошибочные буквы:", end = " ")
    for letter in missedLetters:
        print(letter,end=" ")
    print()

    blanks = "_" * len(secretWord)

    for i in range(len(secretWord)): # заменяет пропуски отгаданными буквами
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # Показывает секретное слово с пробелами между буквами
        print(letter, end=" ")
    print()

def getGuess(alreadyGuessed):
    #Возврашает букву, введенную игроком. Эта функция проверяет, что игрок ввел только одну букву и ничего больше
    while True:
        print("Введите букву.")
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print("Пожалуйста введите одну букву.")
        elif guess in alreadyGuessed:
            print("Вы уже называли эту букву. Назовите другую.")
        elif guess not in "абвгдеёжзиклмнопрстуфхцчшщъыьэюя":
            print("Пожалуйста, введите букву")
        else:
            return guess


def playAgain():
    # Эта функция возвращает значение True, если игрок хочет сыграть заново; в противном случае возвращает False
    print("Хотите сыграть еще? (да или нет)")
    return input().lower().startswith("д")

print("ВИСЕЛИЦА")
missedLetters = ""
correctLetters = ""
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    # Позволяет игроку ввести букву
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters += guess

        # Проверяет, выиграл ли игрок
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print("Да! Секретное слово - \"" + secretWord + "\"! Вы угадали!")
            gameIsDone = True
    else:
        missedLetters += guess

        # Проверяет, превысил ли игрок лимит попыток и проиграл
        if len(missedLetters) == len(HANGMAN_PICS)-1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print("Вы исчерпали попытки!\nБыло загадано " + secretWord)
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ""
            correctLetters = ""
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
        
    
