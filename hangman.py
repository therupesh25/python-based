import random 
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo= ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

                                                                    
                                                                    

word_list=['azure', 
'bagpipes', 
'bandwagon', 
'banjo', 
'bayou', 
'beekeeper', 
'bikini', 
'blitz', ]
random_word=random.choice(word_list)
print(logo)

print(random_word)
h=[]
lives=6

for i in random_word:
    h+='_'
print(h)

game=True
while  game:
    guess=input("enter the letter :").lower()
    for position in range(len(random_word)):
        letter=random_word[position]
        if letter == guess:
            h[position]=letter
    if guess not in random_word:
        lives-=1
        if lives==0:
            game=False
            print("you lose")
    print(f"{' '.join(h)}")
    if "_" not in h:
        game = False
        print("you won ")
    print(stages[lives])


    
    

  
 
