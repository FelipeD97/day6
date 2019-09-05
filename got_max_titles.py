from characters import characters

most_titles = 0
# person_with_most_titles = ''

# visit each character and see if they have more than 'most_titles'
for person in characters:
    num_titles = len(person['titles'])
    if num_titles > most_titles:
        most_titles = num_titles
        # person_with_most_titles = person['name']

# print out the names of each person with same number of titles as 'most_titles'
for person in characters:
    num_titles = len(person['titles'])
    if num_titles == most_titles:
        print('%s has %d titles' % (person['name'], most_titles))