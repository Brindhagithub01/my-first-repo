
'''Exercise: 1
Name your file: NameAnalysis.py
To pass this exercise you must demonstrate that you are able to
Write a program that asks the user to enter his/her full name and the program process and manipulate the text of his/her name.
An example run of the program (numbers in bold are typed in by the user)
Please enter your first name: Peter
Please enter your last name: Cambridge
Your full name is PETER CAMBRIDGE
Your initials are P C
First name length is 5 letters
Last name length is 9 letters
Full name length is 14 letters
First name starts with P
First name ends with R
Last name starts with C
Last name ends with E
First name indexes are 0 – 4
Last name indexes are 0 – 8
First name trims 1 Pet
First name trims 2 eter
Last name trims 1 Cam
Last name trims 2 bridge'''

str1=input("Enter the first name")
str2=input("Enter the last name")
print("Your full name is",str1.upper()+" "+str2.upper())
print("Your initials are",str1[1]+" "+str2[1])
print("First name length is",len(str1),"letters")
print ("last name length is",len(str2),"letters")
print("Full name length is len",len(str1+str2),"letters")
print("First name starts with",str1[1])
print("First name ends with",str1[-1].upper())
print("Last name starts with",str2[1])
print("Last name starts with",str2[-1])
print("First name indexes are 0-",(len(str1)-1))
print("Last name indexes are 0-",(len(str2)-1))
print("First name trims 1",str1[0:4])
print("First name trims 2",str1[4:(len(str1)+1)])
print("Last name trims 1",str2[0:4])
print("Last name trims 2",str2[4:(len(str1)+1)])
