#printing string
Name="Anjani"
print("STRING:",Name)
#length of string
string="Anjani Alaveni"
count=0
for char in string:
 count+=1
print("LENGTH OF STRING: ",count)

#printing each charachter
college="MRCEW"
print("CHARACTER:",end="")
for char in college:
 print(char)
print()
#count the vowels
vowels="alaveni"
count=0
for char in vowels:
 if char in "aeiouAEIOU":
  count=count+1
print("VOWELS COUNT:",count)

#count consonants
consonants="programming"
count=0
for char in consonants:
 if char .isalpha() and char not in "aeiouAEIOU":
  count += 1
print("CONSONANTS:",count)

#uppercase
uppercase="Python Developer"
count=0
for char in uppercase:
 if char .isupper():
  count=count+1
print("UPPERCASE COUNT:",count)

#Lowercase
lowercase="Python Developer"
count=0
for char in lowercase:
 if char .islower():
  count=count+1
print("LOWERCASE COUNT:",count)

#DIGITS
IS_DIGIT="ANJANI1923"
count=0
for char in IS_DIGIT:
 if char .isdigit():
  count=count+1
print("DIGIT COUNT:",count)

#SPECIAL CHARACTERS
IS_SPECIALCHARCTER="ANJANI@1923#"
count=0
for char in IS_SPECIALCHARCTER:
 if not char.isalnum() and char !=" ":
  count=count+1
print("SPECIAL CHARCTERS:",count) 

#COVERT INTO UPPER
WORK="Python Developer"
print("UPPERCASE :", WORK.upper())
#CONVERT INTO LOWER
print("LOWERCASE:",WORK.lower())

#reverseing of string
string1="anjani"
reverse=" "
for char in string1:
 reverse=char+reverse
print("reverse:",reverse) 

#palindrome
pailndrome="Anjani"
reversse=" "
for char in pailndrome:
 reversse=char+reversse
if pailndrome==reversse:
 print(pailndrome,"is a pailndrome")
else:
 print(pailndrome,"is not a Pailndrome")

#FIRST CHARACHTER
string2="Notebook"
print("FIRST_CHARCTER",string2[0])
#LAST CHARACHTER
print("LAST_CHARACHTER",string2[-1])