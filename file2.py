def fac1(num):

    ans=1
    for i in range(1,num+1):
        ans=ans*i

    return ans

def fac2(num):
    if num<=1:
        return 1
    
    return num*fac2(num-1)

num=int(input("enter any no:"))
print(fac1(num))
print(fac2(num))