word = "titans"
print(word.upper())
print(word.capitalize())

def reverse(word):
    if len(word) == 0:
        return word
    else: 
        return reverse (word[1:]) + word[0]
print(reverse (word))