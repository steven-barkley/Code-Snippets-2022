def parse_initials(text):
    initials = text[0]

    for i in range(len(text)):
        if text[i] == " ":
            initials += text[i+1]

    return initials.upper()

def initials_output():
    user_input = input("What is your full name? ")
    
    return "The initials of {0} are {1}".format(user_input,parse_initials(user_input))

if __name__ == "__main__":
    print(initials_output())
