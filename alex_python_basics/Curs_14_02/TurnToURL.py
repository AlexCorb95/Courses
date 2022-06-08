# Fraza = "O #Propoziție ^Este O Succesiune ()De Cuvinte Dintr-o Limbă /Oarecare"


diacritice={
    "ă":"a",
    "â":"a",
    "î":"i",
    "ş":"s",
    "ţ":"t",
    " ":"-",
    "ț":"t"

}


replacebel_char = "ăâîşţț "
char_replacer = "aaistt-"
special_characters = "#^&*()+[]{};',./<>?"

# cu string
def turn_to_url(text):
    text = text.lower()
    result = ""
    for character in text:
        if character in replacebel_char:
            pozitie_diacr = replacebel_char.index(character)
            result = result + char_replacer[pozitie_diacr]
        elif character in special_characters:
            pass
        else:
            result += character
    print(result)
    return result

turn_to_url("ăO #Propoziție ^Este O Succesiune ()De Cuvinte Dintr-o Limbă /Oarecare")

# cu dictionar
def turn_to_url2(text):
    text = text.lower()
    result = ""
    for character in text:
        if character in diacritice:
            result+= diacritice[character]
        elif character in special_characters:
            pass
        else:
            result += character
    print(result)
    return result


turn_to_url2("ăO #Propoziție ^Este O Succesiune ()De Cuvinte Dintr-o Limbă /Oarecare")