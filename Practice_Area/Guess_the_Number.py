"""

This script randomly chooses a number to guess and then the user will have a few chances to guess the number correctly. In each wrong attempt, the computer will give a hint that the number is greater or smaller than the one you have guessed.

"""

import random
import time

c = False
counter = 3

print("Welcome to Digital Game World!!")
name = input("What's your Name?\n")
time.sleep(1)

def ran_1_to_100():
	return random.randrange(1,100)
	
def ran_101_to_1000():
	return random.randrange(101,1000)

def ran_1001_to_10000():
	return random.randrange(10001,100000)
	
def hint_func(user_num, guessed_value, temp_num):
	diff = user_num-guessed_value
	if diff < 0:
		return abs(diff-temp_num), "behind"
	elif diff > 0:
		return diff+temp_num, "ahead"

while True:

	ans = input("Do you want to play a number guessing game?(Y/N) - ").upper()
	
	if ans == "Y" or ans == "YES":
	
		print("\nCool!!")
		time.sleep(0.2)
		print("Tell me what number I am thinking right now. Mind you, you have only 3 attemtpts to guess it right, so GOOD LUCK!!")
		print("And FYI, I will not guess more than 100000 :P :P :P\n")
		choice_func = random.choice([ran_1_to_100,ran_101_to_1000,ran_1001_to_10000])
		guessed_value = choice_func()
		
		while counter>0:
			
			print(f"You have {counter} attemtpt/s left")
			time.sleep(0.2)
			user_num = int(input("\nYour number please - "))
			if user_num == guessed_value:
				print(f"Congrats {name}!! It's a miracle!!! You are a mind reader!! MIND BLOWNNNNNN!!!!")
				c = True
				break
			
			else:
				print("\nSorry!! Your guess is incorrect!!")
				# print(f"****{guessed_value}****")
				counter-=1
				time.sleep(0.3)
				h = True
				while h == True and counter>0:
					hint = input("Do you want to know how behind or ahead are you from my number?(Y/N) - ").upper()
					if hint == "Y" or hint == "YES": 
						hint_val, hint_msg = hint_func(user_num, guessed_value, random.randrange(1,5))
						print(f'I can\'t tell you correctly but you are "ALMOST" {hint_val} {hint_msg} from my guessed number\n')
						h = False
					elif hint == "N" or hint == "NO":
						print("Ok. No Problem. You seem confident :D\n")
						h = False
					else:
						print("Invalid Choice >:(")
						print("Let me ask again")
						time.sleep(0.3)
						
		
		if c:
			break
		else:
			time.sleep(0.4)
			print(f"\nI actually guessed {guessed_value}")
			print(f"Well! Nice playing with you {name}. Goodbye!")
			break
			
			
	elif ans == "N" or ans == "NO":
		print("Ok Bye!! We will meet soon!!")
		break

	else:
		print("Your input is invalid!\n")






