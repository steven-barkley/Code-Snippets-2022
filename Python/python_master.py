#First here is the "main function"

def main():
# Added print function to add space to layout on run
    print('    ')
    print('Learning Python')
    print('    ')

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

if __name__ == '__main__':
    main()
    print(' ')
    user_input()
    print(' ')

def sort_contacts(info):
    key_info = list(info.items())
    key_info.sort()

    sorted_list = []

    for (key,value) in key_info:
        result = (key,value[0],value[1])
        sorted_list += result
    return sorted_list  

sort_contacts({
    #key : value pairs in a dictionary
    "Horney, Karen": ("1-541-656-3010", "karen@psychoanalysis.com"),
    "Welles, Orson": ("1-312-720-8888", "orson@notlive.com"),
    "Freud, Anna": ("1-541-754-3010", "anna@psychoanalysis.com")
    })

#Because I ran a the sort_contacts function the print out will be a alphabetically sorted list
print(sort_contacts({
    #key : value pairs in a dictionary
    "Horney, Karen": ("1-541-656-3010", "karen@psychoanalysis.com"),
    "Welles, Orson": ("1-312-720-8888", "orson@notlive.com"),
    "Freud, Anna": ("1-541-754-3010", "anna@psychoanalysis.com")
    }))



