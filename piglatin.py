## My name is 3lover, and, I am a dragon! I'm also called "Tarin" and lived 5,000 years.
print('Enter the English message to translate into Pig Latin:')
message = input()
vowel = ('a','e','i','o','u')

pigLatin = []
for word in message.split():

  
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]

    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue

    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]

    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower()

    prefixConsonants = ''
    while len(word) > 0 and not word[0] in vowel:
        prefixConsonants += word[0]
        word = word[1:]
    
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else: 
        word += 'yay'
    
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()
    
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

print(' '.join(pigLatin))


