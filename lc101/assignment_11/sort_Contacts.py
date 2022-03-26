def sort_contacts(x):
    for key,value in x:
        return sorted(dict.key(x),dict.value(x))

print(sort_contacts({
    #key : value pairs in a dictionary
    "Horney, Karen": ("1-541-656-3010", "karen@psychoanalysis.com"),
    "Welles, Orson": ("1-312-720-8888", "orson@notlive.com"),
    "Freud, Anna": ("1-541-754-3010", "anna@psychoanalysis.com")
    }))
