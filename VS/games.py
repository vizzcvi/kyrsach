import random

def choose_word():
    words = ["яблоко", "банан", "вишня", "апельсин", "виноград", "киви"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def print_hangman(attempts):
    stages = [
        """
           --------
           |      |
           |      
           |     
           |       
           |         
          ---
        """,
        """
           --------
           |      |
           |      O
           |     
           |       
           |         
          ---
        """,
        """
           --------
           |      |
           |      O
           |      |
           |       
           |         
          ---
        """,
        """
           --------
           |      |
           |      O
           |     /|
           |       
           |         
          ---
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |       
           |         
          ---
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / 
           |         
          ---
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / \\
           |         
          ---
        """
    ]
    
    print(stages[6 - attempts])

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6
    
    print("Добро пожаловать в игру 'Виселица'!")
    
    while attempts > 0:
        display = display_word(word, guessed_letters)
        print("\nСлово: " + display)
        
        guess = input("Угадайте букву: ").lower()
        
        if guess in guessed_letters:
            print("Вы уже угадывали эту букву.")
        elif len(guess) != 1 or not guess.isalpha():
            print("Пожалуйста, введите одну букву.")
        elif guess in word:
            print("Правильно!")
            guessed_letters.append(guess)
        else:
            print("Неправильно!")
            attempts -= 1
            print_hangman(attempts)
        
        if "_" not in display:
            print("\nПоздравляем! Вы угадали слово: " + word)
            break

    if "_" in display:
        print("\nИзвините, вы не угадали слово. Слово было: " + word)

hangman()