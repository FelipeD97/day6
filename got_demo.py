from pprint import pprint
from characters import characters


a_characters = 0 

for character in characters:
    if character['name'][0] == 'A':
        number_characters = len(character)
        print("How many characters names start with \"A\"?") 
        # pprint(character['name'])
        count += 1
        print(count)
        count += 1
    if character['name'].startswith('A') == True:
        pprint(character['name'])


# for character in characters:
#     if character['name'][0] == 'Z':
#         print(character['name'])


# for character in characters:
#     if character['died'] != "":
#         print(character['died'])
#         count += 1
#         print(count)


for character in characters:
    if character['culture'] == 'Valyrian':
        print(character['name'])


# for character in characters:
#     if character['name'] == 'Hot Pie':
#         print(character['playedBy'])


# for character in characters:
#     if 'Targaryen' in character['name']:
#         print(character['name'])

# for character in characters:
#     print
# print(len(characters))

# # print out the key names individually
# for k in jon_snow:
#    print(k)

# # print out just the values
# for key in jon_snow:
#    print(jon_snow[key])

# # print both the key and the value
# for k in characters.jon_snow:
#    print("%s: %s" % (k, jon_snow[k]))

