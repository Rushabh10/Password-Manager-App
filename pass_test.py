file = open("pass.txt", "r")
account_str = file.read()
account_data = eval(account_str)
file.close()

def create_account():
	account = input("Enter the account: ")
	password = input("Enter the password: ")
	account_data[account] = password

def remove_acount():
	account = input("Enter the account you want to remove: ")
	del account_data[account]

def modify():
	account = input("Enter the account you want to change: ")
	password = input("Enter the new password: ")
	account_data[account] = password

def display_pass():
	account = input("Which account password do you want to see: ")
	password = account_data[account]
	print(password)

while(True):
	print("1. Add account")
	print("2. Remove account")
	print("3. Change a password")
	print("4. Check password")
	print("5. Exit")

	selection = int(input(""))

	if selection == 1:
		create_account()
	elif selection == 2:
		remove_acount()
	elif selection == 3:
		modify()
	elif selection == 4:
		display_pass()
	elif selection == 5:
		file = open("pass.txt", "w")
		file.write(str(account_data))
		break
	else:
		print("Invalid selection")








