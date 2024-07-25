from random import randint
def roll():
    return randint(1,6)
    
while True:
    players=input('Enter the number of players (2-4) : ')
    if players.isdigit():
        players=int(players)
        if 2<= players <= 4:
            break
        else:
            print('Enter valid number of players (2-4): ')
    else:
        print('invalid player number')
names=list(map(str,input('Enter player names: ').split()))[:players]
print(names)
winning_score=50
players_score=[0 for i in range(players)]
print(players_score)
while winning_score>max(players_score):
    for i in range(players):
        print("It's player",i+1,'turn')
        print('your present score is: ',players_score[i])
        current_score=players_score[i]
        while True:
            choose=input('would you like to roll (y/Y): ')
            if choose.lower()=='y':
                value=roll()
                if value != 1:
                    current_score=current_score+value
                    print('you rolled : ',value)
                else:
                    current_score=0
                    print('you rolled one so your turn is over')
                    break
            else:
                break
            print('your score is: ',current_score)
        players_score[i]=current_score
        print('your total score is: ',players_score[i])
max_score=max(players_score)
print(names[players_score.index(max_score)],'won the game\nplayer score is :',max_score)



        


