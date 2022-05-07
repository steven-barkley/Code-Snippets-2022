def get_initials(fullname):
		fullname = fullname.split(' ')
		fn = fullname[0]
		sn = fullname[1]
		ln = fullname[2]
		initials = fn[0].upper() + sn[0].upper() + ln[0].upper()
		return initials

def user_input():
		name = input("What is your full name? ")
		print("Your name is {0} and your initials are {1} ".format(name,get_initials(name)))

if __name__ == "__main__":
		user_input()