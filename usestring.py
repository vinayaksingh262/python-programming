str_1= "vinayak"
ch=str_1[4]     #indexing
print(str_1) 
print(ch)    


print(str_1[1:4]) #slicing
print(str_1[0:len(str_1)])#slicing upto last
print(str_1[0:])#slicing upto last
str_2= "singh"                                                               #strings are immutable
name=str_1+str_2
print("hello i am ",name,"and i am learning python",ch)

for character in str_1:   #looping with string
 print(character)
nm="harry is a heera"
print(nm[-4:-2])

#These are string methods

print(str_1.upper())  #all letter in word is capital
print(str_1.lower())  #all letter in word is small

print(str_1.replace("vinayak","mudit"))
print(nm.split(' '))
print(nm.capitalize())
