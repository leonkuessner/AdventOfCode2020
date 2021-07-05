def verify(data):
    new_data = data.split()
    indeces = new_data[0].split("-")
    letters = new_data[1][0]
    password = new_data[2]

    if password[int(indeces[0])-1] == letters and password[int(indeces[1])-1] != letters:
        return True
    elif password[int(indeces[1])-1] == letters and password[int(indeces[0])-1] != letters:#
        return True




with open("d2_input.txt", "r") as f:
    valid_pws = []
    data = f.read().splitlines()
    for i in range(len(data)):
        if verify(data[i]):
            valid_pws.append(data[i])
    print(len(valid_pws))






