
sentence = input('Type in a sentence: ')

#we should ignore words like 'of' from the user input as 'of' is usually not part of acronyms
#we also need to separate each word and store seperately for easy iteration
phrase = (sentence.replace('of','')).split()
# here we use the replace() function to ignore 'of' in the sentence
#and the .split() function to break down the string intp seperate words and store them as a list in phrase 
# we need an empty string variable to store our acronym
acronym = ''

#now we iterate using a for loop through the phrase variable
for word in phrase:
    #we are slicing the first letter of words stored in phrase and adding to our acronym variable
    acronym = acronym + word[0]
    #convert the arconym to capital letter by using the .upper() function
    acronym = acronym.upper()

#finally we print out the statement which will print the acronym
print(f'Acronym of {sentence} is {acronym}')
