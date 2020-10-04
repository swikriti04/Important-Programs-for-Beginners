decimal_num=int(input("Enter the decimal number:"))
binary_num=0
i=0
while(decimal_num!=0):
    remainder=decimal_num%2
    binary_num=decimal_num+remainder*(10**i)
    decimal_num=decimal_num//2
    i=i+1
print("The binary number is :",binary_num)