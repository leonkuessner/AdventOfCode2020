def verify(data, required):
    valid_pps = 0
    for i in range(len(data)):
        # data_dict = dict(zip((data[i][x], data[i][x+1]) for x in range(0, len(data[i]), 2)))
        # print(data_dict)
        # if ['cid'] not in data[i].split(':') and len(data[i]) == len(required):
        #     valid_pps += 1
        #     print(data[i])
        if len(data[i]) == len(required):
            for j in range(len(data[i])):
                fields = data[i][j].split(':')
                if 'cid' in fields:
                    valid_pps += 1
        if len(data[i]) == len(required) + 1:
            valid_pps += 1
            # print(len(data[i]))
    return valid_pps





with open("d4_input", "r") as f:
    data = f.read().split('\n\n')

data_arr = [x.replace('\n', ' ').split() for x in data]
requirements = ['byr','iyr','eyr','hgt', 'hcl', 'ecl', 'pid']
print(verify(data_arr, requirements))

