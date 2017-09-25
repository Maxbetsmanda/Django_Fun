print ("Welcome to the Volleyball Score Program.")

def main():
    team1Wins = []
    team2Wins = []
    matchNum = 1

    while matchNum <= 5:
        a = eval(input("Enter the number of points Team 1 scored in Match " + str(matchNum) + ":" +"\n"))
        b = eval(input("Enter the number of points Team 2 scored in Match " + str(matchNum) + ":" +"\n"))

        if (a>=25 or b>=25):

            if a >= 25 and (abs(a-b)) >= 2:
                    team1Wins.append("win")
                    matchNum += 1

            elif b >= 25 and (abs(b-a)) >= 2:
                    team2Wins.append("win")
                    matchNum += 1

            else:
                print ("That can't be. One team must win by 2 points." + "\n" + "Please reenter the data for Match " + str(matchNum) + ":" + "\n")
                

        else:
            print ("That can't be. One team must get at least 25 points." +"\n" + "Please reenter the data for Match " + str(matchNum) + ":" + "\n")

    #print (team1Wins)
    #print (team2Wins)
    
    if len(team1Wins) > len(team2Wins):
            print ("Team 1 has won the game!")

    elif len(team2Wins) > len(team1Wins):
            print ("Team 2 has won the game!")
main()


        
