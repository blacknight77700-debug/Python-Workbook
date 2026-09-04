items = ['Rock', 'Pogo Stick', 'Wand']
levels = [1, 2, 3]

for level in levels: 
    for item in items:
        if item == 2 and item == 'Rock':
            continue
        else:
            print(f"You can get a {item} at level {level}")
