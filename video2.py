#https://www.youtube.com/watch?v=j31xawnfvXs

given_name = 'Ray'
surname = 'Bates'
age = 45 
favorite_hobby = 'programming in Python'

#string formatting
print(f'{given_name} {surname} is {age} years old. His favorite hobby is {favorite_hobby}')

full_name = 'William John Davis'
age = 18
favorite_hobby = 'motorcycle racing at Kampot'
print ('My name is %s. I am %d years old. My favorite hobby is %s. '%(full_name, age, favorite_hobby))

#print UPPER
print('All caps:', favorite_hobby.upper())

#print lower
print('Lowercase:', favorite_hobby.lower())

#print Capitalize first letter
print('Capitalize only first letter:', favorite_hobby.capitalize())

#print Title Case
print('Title Case:',favorite_hobby.title())

numchars=len(favorite_hobby)
print('There are',numchars, 'characters in',favorite_hobby)

#find the index of a letter
print('The index of the letter a in the word', full_name,'is', full_name.index('a'))

#count frequency of letters
print('There is', full_name.count('a'), 'letter a in the word', full_name)

mylist = full_name.split(' ')
print(mylist)
print ('The first name is %s, the middle name is %s, and the lastname is %s'%(mylist[0], mylist[1], mylist[2]))


