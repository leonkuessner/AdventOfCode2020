with open("d4_input") as fp:
    lines = [f.strip() for f in fp]

#1
curr_passport = {}
all_passports = []
valid_passports = []
all_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
req_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
key_count = 0
for line in lines:
    if line != "":
        temp_line = line.split(" ")
        temp_dict = {item.split(":")[0]:item.split(":")[1] for item in temp_line}

        for key, value in temp_dict.items():
            curr_passport[key] = value

    else:
        if all(field in curr_passport for field in req_keys):
            valid_passports.append(curr_passport)
        curr_passport = {}
        all_passports.append(curr_passport)
all_passports.append(curr_passport)

print(len(all_passports)), print(len(valid_passports))      