def array_of_names(persons):
    list_persons = []
    for fname, lname in persons.items():
        list_persons.append(f"{fname.capitalize()} {lname.capitalize()}")
    return list_persons

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
print(array_of_names(persons))