import random    #inbuilt library for picking random char
import string    #inbuilt library for picking string
print("PLEASE ENTER DESIRED LENGTH OF PASSWORD")
length=int(input())
print("USE COMBINATION OF CHARACTERS TO GENERATE THE PASSWORD" )
print("\n  1- ALPHABET ,\n  2-DIGIT ,\n  3-SPECIAL SYMBOL ,\n  4-EXIT");     
passwordList = ""
#FOR PRINTING COMBINATION OF CHARACTER IN PASSWORD
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
for i in range(4):
	ch = int(input("enter a choice ")) #print for picking a choice
	if(ch == 1):	
		passwordList += string.ascii_letters
	elif(ch == 2):
		passwordList += string.digits
	elif(ch == 3):
		passwordList += string.punctuation
	elif(ch == 4):
		break
	else:
		print("Invalid choice") #print invalid choice
generatedpassword = []
for i in range(length):
	randomchar = random.choice(passwordList)
	generatedpassword.append(randomchar)
print("GENERATED PASSWORD IS:-" + "".join(generatedpassword)) # printing password as a string
