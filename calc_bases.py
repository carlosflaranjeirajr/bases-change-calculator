n=input("Type your data: ")

print('''Choose one of this bases to convert:
        [1] convert to decimal in binary
        [2] convert to decimal in octal
        [3] convert to decimal in hexadecimal
        [4] convert to binary in decimal
        [5] convert to binary in octal
        [6] convert to binary in hexadecimal
        [7] convert to octal in decimal
        [8] convert to octal in binary
        [9] convert to octal in hexadecimal
        [10] convert to hexadecimal in decimal
        [11] convert to hexadecimal in binary
        [12] convert to hexadecimal in octal''')

option=int(input("Choose your option: "))
if option ==1:
    n=int(n)
    print('{} in Binary = {}'.format(n, bin(n)[2:])) 
elif option ==2:
    n=int(n)
    print('{} in Octal = {}'.format(n, oct(n)[2:])) 
elif option ==3:
    n=int(n)
    print('{} in Hexadecimal = {}'.format(n, hex(n)[2:])) 
elif option ==4:
    MyBinDec=int(n,2)
    print(n, 'in Decimal =', MyBinDec)
elif option ==5: 
    MyBinOct=int(n,2)
    print(n, 'in Octal =', oct(MyBinOct)[2:])
elif option ==6:  
    MyBinHex=int(n,2)
    print(n, 'in Hexadecimal =', hex(MyBinHex)[2:])   
elif option ==7:  
    MyOctaDecimal = str(int(n, 8));
    print(n,"in Decimal =",MyOctaDecimal);
     
elif option ==8:  
    num = str(int(n, 8));
    MyOctaBin = int(num);
    print(n,"in Binary =",bin(MyOctaBin)[2:]);
elif option ==9:  
    num = str(int(n, 8));
    MyOctahexa = int(num);
    print(n,"in Hexadecimal =",hex(MyOctahexa)[2:]); 
elif option ==10:
    s = n
    MyHexaDec = int(s, 16)
    str(MyHexaDec)
    print(n,"in Decimal =",MyHexaDec) 
elif option ==11:
   s = n
   MyHexaBin = int(s, 16)
   str(MyHexaBin)
   print(n,"in Binary =",bin(MyHexaBin)[2:])
elif option ==12:
   s = n
   MyHexaOcta = int(s, 16)
   str(MyHexaOcta)
   print(n,"in Octal =",oct(MyHexaOcta)[2:])

else:
    print("Error")  