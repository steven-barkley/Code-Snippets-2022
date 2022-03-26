def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    split_un = fullname.split(" ")
    first_last_ini = [letter[0] for letter in split_un]
    joined_un= "".join(first_last_ini)
    cap_ini = joined_un.upper()
    return cap_ini

def main():
    user_name = input("What is your full name? ")
    print("The initials of " + user_name + " are " + get_initials(user_name))

if __name__ == "__main__":
    main()