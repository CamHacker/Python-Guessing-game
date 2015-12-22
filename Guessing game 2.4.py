#Cameron Barratt 9.04.2014 - 22.12.2015

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
print "Camm's guessing game"
printLines(22)

#defining the varibles
names = []
numOfTrys = []
numAiOfTrys = []
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
Aiconfig=0
low = 1 
high = 0

#gets how many players
print"how many human players"
numOfPlayers = input(">>>")
printLines(22)

#gets the players names
while i != (numOfPlayers + 1):
	if numOfPlayers > 1:
		print"player %r s name" % i
		names.append(raw_input())
		i = i + 1
		printLines(22)

	elif numOfPlayers == 1:
		print"Whats your name"
		names.append(raw_input())
		i = i + 1
		printLines(22)
		
		print"Do you want an AI y or n"
		if raw_input("y/n >") == "y":
			Ai = 1
			names.append("AI")		
				
#gets the highest number the user wants    
print"Whats the highest number you want"
highest = raw_input(">>>")
high = int(highest)
score = int(highest)
printLines(22)

def winners():
	#print how many turns everyone took
	i = 0       
	for x in range(0,(numOfPlayers)):
		print "%r had %r turns" % (names[i],numOfTrys[i])
		i = i + 1

	if winner != "Tie":
		#print who won  
		print"***********************"
		print"winner is %r " % winner
		print"***********************"

	else:
		print"Its a tie"    
		
Aihigh = highest   
#sets the random number for player one
num = random.randint(1, int(highest))

#if theres an Ai set the players to 2 
if Ai == 1:
	numOfPlayers = 2

#main game loop
while whosTurn < numOfPlayers:
	print(" %r guess a number between %s and %s ") %(names[whosTurn],lowest,highest)
	if Ai == 0 or (Ai == 1 and whosTurn == 0):
		guess = raw_input()
		i = int(guess)
	if Ai == 1 and whosTurn == 1:		
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
			  
		elif amountOfTrys == score: #its a tie 
				score = amountOfTrys
				winner = "Tie"       
						
		amountOfTrys = 1
		printLines(22)
		printLines(22)
		
		whosTurn = whosTurn + 1 #run the loop again 
		
	#if the guess is to small 	
	elif i < num:
		print'Try higher'
		if i > lowest:
			lowest = i 
		amountOfTrys = amountOfTrys + 1
		if Ai == 1 and whosTurn == 1:			
			low = i 
				
	#if the guess is to high 	
	elif i > num:
		print'Try lower'
		if i < highest:
			highest = i
		amountOfTrys = amountOfTrys + 1
		if Ai == 1 and whosTurn == 1:			
			high = i

#call the winners function
winners()

