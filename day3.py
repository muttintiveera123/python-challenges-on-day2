#day 3 python program to print smallest vowel at odd repeating
'''n=input("enter the string")
s1=""
for i in range(len(n)):
    if(n[i] in "aeiouAEIOU"):
        if(i%2!=0):
            s1+=n[i]
print(min(s1))'''
#or
'''s=input("enter the name")
s1=""
for i in s:
    if i in"aeiouAEIOU":
        if s.count(i)%2!=0:
            s1+=i
print(min(s1))'''
# reorder string
'''n=input("enter the name")
s="codeforces"
count=0
for i in range(len(n)):
    if(s[i]!=n[i]):
        count=count+1
print(count)'''
#reorder
'''n=input("enter the name")
s="codeforces"
count=0
s1=""
s2=""
for i in range(len(n)):
    if(s[i]!=n[i]):
        count=count+1
        s1+=s[i]
        s2+=n[i]
print(s2)
print(s1)
print(count)'''

#to check 
'''n,p=map(str,input("enter two strings").split(" "))
s1=""
s2=""
for i in p:
    if(i not in n):
        s1+=i
    else:
        s2
print(s1)
print(s2)'''
# program make encryption and decryption with key value using functions
'''def encrypt(n,p):
    s1=""
    for i in n:
        r=ord(i)
        k=r+p
        s1+=chr(k)
    print(s1)
def decrypt(n,p):
    s2=""
    for i in n:
        r=ord(i)
        k=r-p
        s2+=chr(k)
    print(s2)
n=input("enter the string") 
p=int(input("enter the number"))
op=input("enter the operation")
if op=="encrypt":
    encrypt(n,p)
elif op=="decrypt":
    decrypt(n,p)
else:
    print("no operation")'''

#insert digit as large as possible
'''s,d=map(str,input("enter the digits and number").split(" "))
for i in range(len(s)):
    if(int(s[i]) <= int(d)):
        print(s[:i]+d+s[i:])
        break
else:
    print(s+d)'''
#python armstrong in a range using strings and functions

'''def armstrong(n,p):
    for i in range(n,p):
        s=str(i)
        sum=0
        for j in s:
            sum+=int(j)**len(s)
        if str(sum)==s:
            print(i)
n,p=map(int,input("enter the n and p").split(" "))
armstrong(n,p)'''
#recursion
# to print n natural numbers recursion
'''def recur(n):
    if n < 1:
        return 1
    else:
        recur(n-1)
        print(n)
n=int(input("enter the value "))
recur(n)'''
#sum of digits
'''def sumofdigits(n):
    if n<1:
        return 1
    else:
        return sumofdigits(n-1)+n
n=int(input("enter the value"))
print(sumofdigits(n))'''

#fact
'''def fact(n):#5
    if(n==1):
        return 1
    else:
        factorial= n*fact(n-1)
        return factorial #5*fact(4) 
# strong numbers in range using strings
def strong(x):
    s=str(x)
    sum=0
    for i in s:
        sum+=fact(int(i))
    if sum==x:
        return "strong number"
    else:
        return "not a strong number"
x=int(input())
print(strong(x))'''
# strong number in range
'''def fact(n):#5
    if(n<1):
        return 1
    else: 
        return n*fact(n-1)#5*fact(4) 
def strong(x):
    s=str(x)
    sum=0
    for i in s:
        sum+=fact(int(i))
    if sum==x:
        print(x)
a,b=int(input()),int(input())
for i in range(a,b+1):
    strong(i)'''
#strings
'''l=list(int(input("enter the elements")).split(" "))
l1=[]
for i in range(1,len(l)):
    if(l[i-1]==l[i]):
        l1.append(i)
print(l1)'''
#
'''l=list(input())
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)'''

#odds
'''print(sum([i for i in range(1,11) if i%2!=0]))'''

#sum of odd composite numbers
def composite_numbers(n):
    sum=0
    for i in range(1,n+1):
        if (n%i==0):
            sum+=i
    if sum>2:
        return 1
    else:
        return 0
a,b=map(int,input("enter the range").split(" "))
l1=[]
for i in range(a,b+1):
    if(i%2!=0):
        flag=composite_numbers(i)
        if flag == 1:
            l1.append(i)
print(sum(l1))
print(l1)














         
    

        
    






        













        
