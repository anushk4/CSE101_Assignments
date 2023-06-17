def threedigit(n,d1,d2,d3):
    if n%100==0:
        return d1[n//100]+" hundred"
    if n//100==0:
        return twodigit(n-100*(n//100),d1,d2,d3)
    else:
        return d1[n//100]+" hundred "+twodigit(n-100*(n//100),d1,d2,d3)

def twodigit(n,d1,d2,d3):
    if n>=0 and n<=9:
        return d1[n]
    elif n>10 and n<=19:
        return d2[n]
    elif n%10==0:
        return d3[n//10]
    else:
        return d_tens[n//10]+" "+d_ones[n%10]
    
def fourdigit(n,d1,d2,d3):
    if n%1000==0:
        return d1[n//1000]+" thousand"
    elif n//1000==0:
        return threedigit(n-1000*(n//1000),d1,d2,d3)
    else:
        return d1[n//1000]+" thousand "+threedigit(n-1000*(n//1000),d1,d2,d3)
    
def fivedigit(n,d1,d2,d3):
    if n%1000==0:
        return twodigit(n//1000,d1,d2,d3)+" thousand "
    elif n//10000==0:
        return fourdigit(n-10000*(n//10000),d1,d2,d3)
    else:
        return twodigit(n//1000,d1,d2,d3)+" thousand "+threedigit(n-1000*(n//1000),d1,d2,d3)
    
def sixdigit(n,d1,d2,d3):
    if n%100000==0:
        return d1[n//100000]+" lakh"
    elif n//100000==0:
        return fivedigit(n-100000*(n//100000),d1,d2,d3)
    else:
        return d1[n//100000]+" lakh "+fivedigit(n-100000*(n//100000),d1,d2,d3)
    
def sevendigit(n,d1,d2,d3):
    if n%100000==0:
        return twodigit(n//100000,d1,d2,d3)+" lakh "
    elif n//1000000==0:
        return sixdigit(n-1000000*(n//1000000),d1,d2,d3)
    else:
        return twodigit(n//100000,d1,d2,d3)+" lakh "+fivedigit(n-100000*(n//100000),d1,d2,d3)
    
def eightdigit(n,d1,d2,d3):
    if n%10000000==0:
        return d1[n//10000000]+" crore "
    elif n//10000000==0:
        return sevendigit(n-10000000*(n//10000000),d1,d2,d3)
    else:
        return d1[n//10000000]+" crore "+sevendigit(n-10000000*(n//10000000),d1,d2,d3)
    
def ninedigit(n,d1,d2,d3):
    if n%10000000==0:
        return twodigit(n//10000000,d1,d2,d3)+" crore "
    elif n//100000000==0:
        return eightdigit(n-100000000*(n//100000000),d1,d2,d3)
    else:
        return twodigit(n//10000000,d1,d2,d3)+" crore "+sevendigit(n-10000000*(n//10000000),d1,d2,d3)

def d_name(n,d1,d2,d3):
    if n<=99:
        print(twodigit(n,d1,d2,d3))
    elif n<=999:
        print(threedigit(n,d1,d2,d3))
    elif n<=9999:
        print(fourdigit(n,d1,d2,d3))
    elif n<=99999:
        print(fivedigit(n,d1,d2,d3))
    elif n<=999999:
        print(sixdigit(n,d1,d2,d3))
    elif n<=9999999:
        print(sevendigit(n,d1,d2,d3))
    elif n<=99999999:
        print(eightdigit(n,d1,d2,d3))
    elif n<=999999999:
        print(ninedigit(n,d1,d2,d3))

d_ones={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
d_11to19={11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}
d_tens={1:"ten",2:"twenty",3:"thirty",4:"forty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninety"}
n=int(input("Enter number: "))
d_name(n,d_ones,d_11to19,d_tens)