import string

given_string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"

alphabets = string.ascii_lowercase



def translator(given_string, alphabets):
    new_string = ''
    for letter in given_string:
        if alphabets.find(letter) == -1:
            new_string += letter
            continue

        position = alphabets.find(letter) + 2

        if position >= 26:
            position = position - 26

        #print(alphabets.find(letter))

        new_string += alphabets[position]

    print(new_string)

translator(given_string, alphabets)

url_string = 'map'

translator(url_string, alphabets)
