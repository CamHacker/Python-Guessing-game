#Cameron Barratt 9.04.2014 - 23.12.2015

#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

#imports the random mod and time
import time
import random

#a function that prints lines when called
def printLines(amountOfLines):
	print "-" * amountOfLines

 #prints the welcome box    
printLines(22)
print "     Welcome"
print "       To"
print "Cam's guessing game"
printLines(22)

#defining the global varibles
names = []
numOfTrys = []
numAiOfTrys = []
numOfPlayers = 0
Ainum = 0
i = 1
whosTurn = 0
amountOfTrys = 1
amountOfAiTrys = 1
highest = 0
lowest = 1
Ai = 0
Ainumtoguess = 0
score = 0
lowestscore = 0
Aiconfig=0
low = 1 
high = 0
winnernum = 0
losernum = 0
isint = 0
answer ="nil"
amountOfAIs = 0
numOfHumanPlayers = 0


while True:
    try:
        numOfPlayers=int(raw_input('how many players?: '))
        numOfHumanPlayers = numOfPlayers
        printLines(22)
        break
    except ValueError:
        print ("Error Please enter a vaild number and not a letter")
        printLines(22)
        	
#gets the players names
while i != (numOfPlayers + 1):
	if numOfPlayers > 1:
		print"player %r's name" % i
		names.append(raw_input())
		i = i + 1
		printLines(22)

	elif numOfPlayers == 1:
		print"Whats your name"
		names.append(raw_input())
		i = i + 1
		printLines(22)
		
		while True:
			print"Do you want an AI y or n"
			answer = raw_input("y/n > ")
			if answer == "y" or answer == "Y":
				Ai = 1
				print"how many ?"
				amountOfAIs = int(raw_input("> "))
				for x in range(0,amountOfAIs):
					names.append("AI " + str((x + 1))) #TODO add random names 
					
				printLines(22)
				break 
				
			elif answer == "n" or answer == "N":
				printLines(22)
				break
			else:
				print "enter a vaild choice please"		
			printLines(22)	

			
#gets the highest number the user wants and check for an answer
while True:
    try:
		highest=int(raw_input('Whats the highest number you want?:'))
		high = int(highest)
		score = int(highest)
		break
    except ValueError:
        print ("Error Please enter a vaild number and not a letter")
        
	printLines(22)   

#find our who won and how many turns everyone took
def winners():
	#print how many turns everyone took
	i = 0       
	for x in range(0,(numOfPlayers)):
		if x == winnernum:
			print "%s had %s turns(winner)" % (names[i],numOfTrys[i])
		elif x == losernum:
			print "%s had %s turns and lost by %s turns(worst)" % (names[i],numOfTrys[i],(numOfTrys[i] - numOfTrys[winnernum]))
		else:
			print "%s had %s turns and lost by %s turns" % (names[i],numOfTrys[i],(numOfTrys[i] - numOfTrys[winnernum]))
		i = i + 1

	if winner != "Tie":
		#print who won  
		print"%s**********************" %("*" * len(winner)) 
		print"winner is %s , Congrats!" % winner
		print"%s**********************"%("*" * len(winner)) 

	else:
		print"Its a tie"    
		
Aihigh = highest   
#sets the random number for player one
num = random.randint(1, int(highest))

#if theres an Ai set the players to 2 
if Ai == 1:
	numOfPlayers += amountOfAIs
	
memhigh = highest



#main game loop
while whosTurn < numOfPlayers:
	print(" %r guess a number between %s and %s ") %(names[whosTurn],lowest,highest)
	if Ai == 0 or (Ai == 1 and whosTurn == 0):
		guess = raw_input()
		i = int(guess)
	if Ai == 1 and whosTurn >= numOfHumanPlayers:		
		time.sleep(1)
		guess = random.randint(int(low+1),int(high-1)) #added this to fix AI
		i = int(guess)
		print "Ai's guess is %s"%guess
		printLines(22)
		time.sleep(1)
		
	 #if the guessed nunber is the random it changes the players turn or ends the guessing
	if i == num:
		numOfTrys.append(amountOfTrys)
		#numOfTrys.append(amountOfTrys)
		print'You guessed right'
		print "Number of trys :%r" % amountOfTrys
		num = random.randint(1,int(highest)) #changes the random number for the next player


		if amountOfTrys < score:#find out who will be the winner
			  score = amountOfTrys
			  winner = names[whosTurn]
			  winnernum = whosTurn
			  
		elif amountOfTrys > lowestscore:#find out who will have the worst score
			  lowestscore = amountOfTrys
			  loser = names[whosTurn]
			  losernum = whosTurn
			  
		elif amountOfTrys == score: #its a tie 
				score = amountOfTrys
				winner = "Tie"       
										
		amountOfTrys = 1
		printLines(22)
		printLines(22)
		
		lowest = 1
		
		#Ai 
		low = 1
		high = memhigh
		
		highest = memhigh
		whosTurn = whosTurn + 1 #run the loop again 
		
		
	#if the guess is to small 	
	elif i < num:
		print'Try higher'
		if i > lowest:
			lowest = i 
		amountOfTrys = amountOfTrys + 1
		if Ai == 1 and whosTurn >= numOfHumanPlayers:			
			low = i 
				
	#if the guess is to high 	
	elif i > num:
		print'Try lower'
		if i < highest:
			highest = i
		amountOfTrys = amountOfTrys + 1
		if Ai == 1 and whosTurn >= numOfHumanPlayers:			
			high = i
			
	if amountOfTrys == 5:
		printLines(22)
		print "comme on you can do better than this!" #TODO add random messages from a list or file #fix print this on every line with varible
		printLines(22)
		
	if amountOfTrys  == 10:
		printLines(22)
		print "Wow whats taking so long ?" #TODO add random messages from a list or file
		printLines(22)
		
	if amountOfTrys  == 15:
		printLines(22)
		print "15 turns ? we waiting you know?" #TODO add random messages from a list or file
		printLines(22)

#call the winners function
winners()

