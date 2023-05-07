'''Exercise: 2
Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2'''


n=int(input("enter the range"))
list=[]
for i in range(0,n):
    m=input("enter the string")
    list.insert(i,m)
print(list)
count = 0
for m in list:
  if len(m)>=2 and m[0]==m[-1]:
            count=count+1
print("Expected Result",count)
