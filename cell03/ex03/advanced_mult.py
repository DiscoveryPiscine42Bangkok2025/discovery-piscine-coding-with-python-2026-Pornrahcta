i = 0
table = []
while i < 11:
    j = 0
    while j < 11:
        table.append(f"{i*j}")
        j += 1
    print(f"Table de {i}: {' '.join(table)}")
    table = []
    i += 1