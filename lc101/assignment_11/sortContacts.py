# Create sort_contacts function
def sort_contacts(contacts):
    #Order my dictionary by string names
    key_c = list(contacts.items())
    key_c.sort()
    mylist = []
    for (k,v) in key_c:
        result = (k,v[0],v[1])
        mylist += result
    return mylist

sort_contacts({
    #key : value pairs in a dictionary
    "Horney, Karen": ("1-541-656-3010", "karen@psychoanalysis.com"),
    "Welles, Orson": ("1-312-720-8888", "orson@notlive.com"),
    "Freud, Anna": ("1-541-754-3010", "anna@psychoanalysis.com")
    })

    #tuples in a list
print([('Freud, Anna', '1-541-754-3010', 'anna@psychoanalysis.com'), 
    ('Horney, Karen', '1-541-656-3010', 'karen@psychoanalysis.com'), 
    ('Welles, Orson', '1-312-720-8888', 'orson@notlive.com')])