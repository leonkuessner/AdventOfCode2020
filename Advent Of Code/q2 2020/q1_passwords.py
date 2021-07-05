def verify(data):
    new_data = data.split()
    lengths = new_data[0].split("-")
    letter = new_data[1][0]
    password = new_data[2]

    letters_pw = password.count(letter)
    if letters_pw >= int(lengths[0]) and letters_pw <= int(lengths[1]):
        return True
    else:
        return False

with open("d2_input.txt", "r") as f:
    valid_pws = []
    data = f.read().splitlines()
    for i in range(len(data)):
        if verify(data[i]):
            valid_pws.append(data[i])
    print(len(valid_pws))