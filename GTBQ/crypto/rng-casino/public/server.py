import random
from secret import FLAG
class Casino:
    def __init__(self) -> None:
        self.money = 100
        
    def high_low(self) -> None:
        if self.money < 10:
            print('You need at least $10 to play this game')
            return
        self.money -= 10
        black=random.getrandbits(1)
        guess=input('Guess the color of the Ball: (b/w) ')
        if (guess == 'b' and black) or (guess == 'w' and not black):
            self.money += 18
            print('You guessed it right!')
        else: 
            print('You guessed it wrong sorry!')
        
    def guess(self) -> None:
        while True:
            choice=input('\nWould you like to play for a chance to win (entry is 40$) or practice? (play/practice): ')
            if choice in ['play','practice']:
                practice=choice=='practice'
                break
            print('Invalid choice!\n')
        if not practice and self.money < 40:
            print('You need at least $40 to play this game')
            return
        if not practice:
            self.money -= 40
            
        guess = int(input('Guess the number > '))
        my_num=random.getrandbits(128)
        if guess == my_num:
            print(f'Wow you are either really lucky, or practice makes perfect!')
            if not practice:
                self.money += 13371337
        else:
            print('Nope, the number was '+str(my_num)+'\n') 
        
    def lobby(self):
        print('Welcome to the RNG-Casino!!')
        while True:
            print('\nWhat would you like to play?\n1. Black or White Ball (10$)\n2. Guess the number (40$ or practice)\n3. Buy flag\n4. Exit\n')
            choice = input(f'You have {self.money}$! Enter your choice: ')
            if choice == '1':
                self.high_low()
            elif choice == '2':
                self.guess()
            elif choice == '3':
                if self.money < 1000000:
                    print('You need at least $1000000 to buy the flag')
                    continue
                print(f'Here\'s your flag: {FLAG}')
            elif choice == '4':
                print('Goodbye')
                break
            else:
                print('Invalid choice')

        
casino = Casino()
casino.lobby()