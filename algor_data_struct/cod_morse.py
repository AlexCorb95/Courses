MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
              '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I',
              '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N',
              '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S',
              '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W',
              '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1',
              '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6',
              '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?',
              '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&',
              '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_',
              '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS',
              }


def decode_morse (morse_code: str) -> str:
    morse_code_trans=""
    if "   " in morse_code:
        morse_lst=morse_code.split("   ")
        for items in morse_lst:
            morse_code_trans+=" "
            item_lst = items.split()
            for item in item_lst:

                if item in MORSE_CODE:
                    morse_code_trans+="".join(MORSE_CODE[item])
    else:
        morse_lst = morse_code.split()
        for item in morse_lst:

            if item in MORSE_CODE:
                morse_code_trans += "".join(MORSE_CODE[item])
    return print(morse_code_trans)

decode_morse ('.... . -.--   .--- ..- -.. .')
decode_morse(' . ')
decode_morse('...   ---   ...')