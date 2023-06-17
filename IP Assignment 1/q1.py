def d_name(n,d1,d2,d3):
    if n>=0 and n<=9:
        print(d1[n])
    elif n>10 and n<=19:
        print(d2[n])
    elif n%10==0:
        print(d3[n//10])
    else:
        print(d_tens[n//10]+" "+d_ones[n%10])

d_ones={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
d_11to19={11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}
d_tens={1:"ten",2:"twenty",3:"thirty",4:"forty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninety"}
n=int(input("Enter number: "))
d_name(n,d_ones,d_11to19,d_tens)