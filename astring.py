# 1. taking input from user
str = input('enter first name ')
st = int(len(str))
print(' length of the string is  %d' %st)

# 2. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
print(str[:2]+str[-2:])

''' 3. Write a Python program to get a single string from two given strings by user , separated by a space and swap the first two characters of each string. 
Sample String : 'abc', 'xyz' 
Expected Result : 'xyc abz'''

str1 = input('enter last name ')
str2 = str1[:2] + str[2:] +' ' + str[:2] + str1[2:]
print(str2)

''' 4. Write a Python program to change a given string to a new string where all
 the even position characters are in starting and all odd position characters are in end.'''
str = str[0::2]+str[1::2]
print(str)

''' 5. Write a Python program to remove the characters which have odd index values of a given string'''
str3 = input('enter a new string ')
result = ""
for i in range(len(str3)):
	if i % 2 == 0:
		result = result + str3[i]

print(result)

print(str3.replace(str3[1::2],'')) #dosnt work
print(str.replace(str[1::2],''))   #works

''' 6. WAP to insert a string in the middle of a other string.'''

word = input('insert a string in the middle ' )
mid = int(len(str3)/2)
print(mid)
print(str3[:mid]+word+str3[mid:])
