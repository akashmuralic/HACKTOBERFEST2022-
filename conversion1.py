print('''Enter your choice 
      a for decimal to Binary
      b for binary to decimal''')
ch=input("enter your choice\n")
n=int(input("Enter your number according to your choice\n"))

def DecimalToBinary(num):
     
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end = '')
    
def binaryToDecimal(binary):
     
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    print(decimal)   
    
if ch is "a":
    DecimalToBinary(n)
elif ch is "b":
    binaryToDecimal(n)
else:
    print("invalid input")
