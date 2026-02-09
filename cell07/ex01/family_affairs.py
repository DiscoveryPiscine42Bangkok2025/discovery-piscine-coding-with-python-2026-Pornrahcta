def find_the_redheads(persons):
    list_persons = []
    filtered_by_color = [key for key, value in persons.items() if value == "red"]
    return filtered_by_color

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))