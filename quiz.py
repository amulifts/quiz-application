# JSON is a syntax for storing and exchanging data.
# Python has a built-in package called json, which can be used to work with JSON data.
import json
# Python Random module is an in-built module of Python which is used to generate random numbers. 
import random
# No echo input ( passwords aren't shown )
import getpass

user = []

def play():
	print("\n==========QUIZ START==========")
	score = 0
	with open("assets/questions.json", 'r+') as f:
		j = json.load(f)
		for i in range(10):
			no_of_questions = len(j)
			ch = random.randint(0, no_of_questions-1)
			print(f'\nQ{i+1} {j[ch]["question"]}\n')
			for option in j[ch]["options"]:
				print(option)
			answer = input("\nEnter your answer: ")
			if j[ch]["answer"][0] == answer[0].upper():
				print("\nYou are correct")
				score+=1
			else:
				print("\nYou are incorrect")
			del j[ch]
		print(f'\nFINAL SCORE: {score}')

def quizQuestions():
	if len(user) == 0:
		print("You must first login before adding questions.")
	elif len(user) == 2:
		if user[1] == "ADMIN":
			print('\n==========ADD QUESTIONS==========\n')
			ques = input("Enter the question that you want to add:\n")
			opt = []
			print("Enter the 4 options with character initials (A, B, C, D)")
			for _ in range(4):
				opt.append(input())
			ans = input("Enter the answer:\n")
			with open("assets/questions.json", 'r+') as f:
				questions = json.load(f)
				dic = {"question": ques, "options": opt, "answer": ans}
				questions.append(dic)
				f.seek(0)
				json.dump(questions, f)
				f.truncate()
				print("Question successfully added.")		
		else:
			print("You don't have access to adding questions. Only admins are allowed to add questions.")

def createAccount():
	print("\n==========CREATE ACCOUNT==========")
	username = input("Enter your USERNAME: ")
	password = getpass.getpass(prompt= 'Enter your PASSWORD: ') # The getpass() function is used to prompt to users using the string prompt and reads the input from the user as Password.
	with open('assets/user_accounts.json', 'r+') as user_accounts: #The r+ mode is used to open a file for both reading and writing
		users = json.load(user_accounts)
		if username in users.keys():
			print("An account of this Username already exists.\nPlease enter the login panel.")
		else:
			users[username] = [password, "PLAYER"]
			user_accounts.seek(0) # seek() function is used to change the position of the File Handle to a given specific position. 0 = beginnning
			json.dump(users, user_accounts) #dumps convert python objects of the all types such int,float,list,tuple,dictionary into JSON strings:
			user_accounts.truncate() # Python file method truncate() truncates the file's size.
			print("Account created successfully!")

def loginAccount():
	print('\n==========LOGIN PANEL==========')
	username = input("USERNAME: ")
	password = getpass.getpass(prompt= 'PASSWORD: ')
	with open('assets/user_accounts.json', 'r') as user_accounts:
		users = json.load(user_accounts)
	if username not in users.keys():
		print("An account of that name doesn't exist.\nPlease create an account first.")
	elif username in users.keys():
		if users[username][0] != password:
			print("Your password is incorrect.\nPlease enter the correct password and try again.")
		elif users[username][0] == password:
			print("You have successfully logged in.\n")
			user.append(username)
			user.append(users[username][1])

def logout():
	global user
	if len(user) == 0:
		print("You are already logged out.")
	else:
		user = []
		print("You have been logged out successfully.")

def rules():
	print('''\n==========RULES==========
1. Each round consists of 10 random questions. To answer, you must press A/B/C/D (case-insensitive).
Your final score will be given at the end.
2. Each question consists of 1 point. There's no negative point for wrong answers.
3. You can create an account from ACCOUNT CREATION panel.
4. You can login using the LOGIN PANEL. Currently, the program can only login and not do anything more.
	''')

def about():
	print('''\n==========ABOUT US==========
This project has been created by Aman Khadka.
It is a basic Python Project for my 1st Semester.''')

if __name__ == "__main__":
	choice = 1
	while choice != 7:
		print('\n=========WELCOME TO QUIZ MASTER==========')
		print('-----------------------------------------')
		print('1. PLAY QUIZ')
		print('2. ADD QUIZ QUESTIONS')
		print('3. CREATE AN ACCOUNT')
		print('4. LOGIN PANEL')
		print('5. LOGOUT PANEL')
		print('6. SEE INSTRUCTIONS ON HOW TO PLAY THE GAME')
		print('7. EXIT')
		print('8. ABOUT US')
		choice = int(input('ENTER YOUR CHOICE: '))
		if choice == 1:
			play()
		elif choice == 2:
			quizQuestions()
		elif choice == 3:
			createAccount()
		elif choice == 4:
			loginAccount()
		elif choice == 5:
			logout()
		elif choice == 6:
			rules()
		elif choice == 7:
			break
		elif choice == 8:
			about()
		else:
			print('WRONG INPUT. ENTER THE CHOICE AGAIN')