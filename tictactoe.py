import os
import random
from itertools import combinations
def board(board):
	os.system('cls')
	print("    |    |    ")
	print(" {} | {} | {} ".format(board[6],board[7],board[8]))
	print("    |    |    ")
	print("____|____|____")
	print("    |    |    ")
	print(" {} | {} | {} ".format(board[3],board[4],board[5]))
	print("    |    |    ")
	print("____|____|____")
	print("    |    |    ")
	print(" {} | {} | {} ".format(board[0],board[1],board[2]))
	print("    |    |    ")

def first(name1,name2):
	x=int(random.randint(0,9))
	if(x<=5):
		return name1
	else:
		return name2

def game(a,XO,Xa,Oa,k,n,name1,m,name2):
	print(name1,"will go first")
	for i in XO:
		if i==n and k==0:
			board(a)
			k=position(a,Xa,k,n,name1)
		elif i==m and k==0:
			board(a)
			k=position(a,Oa,k,m,name2)
	if(k==0):
		print("It is a tie!!!")

def position(a,Xa,k,n,name):
	pre=[(1,2,3),
		 (4,5,6),
		 (7,8,9),
		 (1,5,9),
		 (3,5,7),
		 (1,4,7),
		 (2,5,8),
		 (3,6,9)]
	
	while (True):
		print(name,":Choose your next position (1-9)")
		next=int(input())
		if (a[next-1]=="  "):
			a[next-1]=" "+n
			Xa.append(next)
			break
		else:
			print("Position already used...Enter again")
      
	#check if the player has won or no
	for i in list(combinations(sorted(Xa),3)):
		for j in pre:
			if i==j:
				board(a)
				print(name," has won!!!")
				print("*******************")
				return 1
				break
			else:
				continue
	return 0

def replay():
	choice=input("Play again?  Enter Yes or No\n")
	return choice=="Yes"		

print("Welcome to tic tac toe!")
while True:
	Xa=[]
	Oa=[]
	k=0
	a=["  ","  ","  ","  ","  ","  ","  ","  ","  "]
	XO=["X","O","X","O","X","O","X","O","X"]
	OX=["O","X","O","X","O","X","O","X","O"]

	#Assigns X or O to the player
	n=input("Player 1:Do you want to be an X or O?").upper()
	if n=="X":
		m="O"
	else:
		m="X"

	#Decides randomly which player goes first
	name=first("Player 1","Player 2")
	if name=="Player 1":
		name1="Player 1"
		name2="Player 2"
	else:
		name1="Player 2"
		name2="Player 1"

	#Game Begin
	if name1=="Player 1":
		if n==XO[0]:
			game(a,XO,Xa,Oa,k,n,name1,m,name2)#X,O
		else:
			game(a,OX,Xa,Oa,k,n,name1,m,name2)
	else:
		if m==XO[0]:
			game(a,XO,Xa,Oa,k,m,name1,n,name2)#X,O
		else:
			game(a,OX,Xa,Oa,k,m,name1,n,name2)
	if not replay():
		break

print("THANK YOU!")
