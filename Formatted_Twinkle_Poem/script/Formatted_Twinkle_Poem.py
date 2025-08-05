poem = "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, " \
"Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
str_list = []
start = 0
stop_characters = [',', '.', '!','?']
for i in range(len(poem)):
    if poem[i-2] in stop_characters and poem[i]==poem[i].upper():
        str_list.append(poem[start:i-1])
        #print(str_list)
        start = i
        if i == len(poem) - 1:
            break
str_list.append(poem[start:])  # Append the last segment
print(str_list)

blanck_space = ' '
for i in range(len(str_list)):
    if str_list[i].startswith('T'):
        print(str_list[i])
    elif str_list[i].startswith('H'):
        print(8*blanck_space+str_list[i])
    else:
        print(16*blanck_space+str_list[i].capitalize())