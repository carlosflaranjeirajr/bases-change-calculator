n=input("Type your data: ") #section to user put your data

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
        [12] convert to hexadecimal in octal''') #list of options for user make a choice

option=int(input("Choose your option: ")) #section to user put your number's option
if option ==1:
    n=int(n)
    print('{} in Binary = {}'.format(n, bin(n)[2:])) #algorithm convert to decimal in binary 
elif option ==2:
    n=int(n)
    print('{} in Octal = {}'.format(n, oct(n)[2:])) #algorithm convert to decimal in octal
elif option ==3:
    n=int(n)
    print('{} in Hexadecimal = {}'.format(n, hex(n)[2:])) #algorithm convert to decimal in hexadecimal
elif option ==4:
    MyBinDec=int(n,2)
    print(n, 'in Decimal =', MyBinDec) #algorithm convert to binary in decimal
elif option ==5: 
    MyBinOct=int(n,2)
    print(n, 'in Octal =', oct(MyBinOct)[2:]) #algorithm convert to binary in octal
elif option ==6:  
    MyBinHex=int(n,2)
    print(n, 'in Hexadecimal =', hex(MyBinHex)[2:]) #algorithm convert to binary in hexadecimal
elif option ==7:  
    MyOctaDecimal = str(int(n, 8))
    print(n,"in Decimal =",MyOctaDecimal)#algorithm convert to octal in decimal
     
elif option ==8:  
    num = str(int(n, 8))
    MyOctaBin = int(num)
    print(n,"in Binary =",bin(MyOctaBin)[2:]) #algorithm convert to octal in binary
elif option ==9:  
    num = str(int(n, 8))
    MyOctahexa = int(num)
    print(n,"in Hexadecimal =",hex(MyOctahexa)[2:]) #algorithm convert to octal in hexadecimal
elif option ==10:
    s = n
    MyHexaDec = int(s, 16)
    str(MyHexaDec)
    print(n,"in Decimal =",MyHexaDec) #algorithm convert to hexadecimal in decimal
elif option ==11:
   s = n
   MyHexaBin = int(s, 16)
   str(MyHexaBin)
   print(n,"in Binary =",bin(MyHexaBin)[2:]) #algorithm convert to hexadecimal in binary
elif option ==12:
   s = n
   MyHexaOcta = int(s, 16)
   str(MyHexaOcta)
   print(n,"in Octal =",oct(MyHexaOcta)[2:])#algorithm convert to hexadecimal in octal

else:
    print("Error")  #Error message