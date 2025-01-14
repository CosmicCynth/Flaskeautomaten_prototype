my_dict = {
    "Bomba": 3,
    "Racoon": 5
}

def pant():
    output = ""
    for key, value in my_dict.items():
        output += f"{key}: {value}\n"
    return output

print(pant())


