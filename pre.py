print("Please enter the number of gift packages with sweets prepared by Bajtek")
n=int(input())                       #input number of gifts, it's natural number in range 1<=n<=200000


sweets=[]                            #creating list for increasing numbers of gits

for i in range (1, n +1):            #loop for adding following elements of list 
    sweets.append(i)
#print(sweets)                       print function for test and show type of sweet list
#print(type(sweets))

even=False
if n%2==0: 
    even=True                          #chcecking if number of gifts is is even. Even numbers are divisible by 2 without remainders.   
    result = []                        #creating list for increasing numbers of gits
    half=int(n/2)
    for j in range(1,half+1):
        result.append(str(j)+" "+str(n-j+1))
        #print(sweets[j-1])
else:
    n=n-1
    #print(n)
    result = []
    half=int(n/2)
    #print(half)
    for j in range(1,half+1):
        result.append(str(j)+" "+str(n-j+1))
    result.insert(half+1,n+1)
print("Number of children who will get equal number of sweets:")
print(len(result))
print("Sets of sweets of fair distribution:")
if even==True:
    for j in range(1,half+1):
        print(result[j-1])
else: 
    for j in range(1,half+2):
        print(result[j-1])

    



