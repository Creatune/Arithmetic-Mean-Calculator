#Arithmetic mean calculator
import time
print("This programme calculates the mean of ungrouped data...")
print("It calculates up to a maximum of **5** observations")
n = input("Type the number of observations -n- value : ")
if n=='1':
    num1 = input("Type the first observation : ")
    print("The arithmetic mean of the given data is =", '**',num1,'**')
else:
    print('')
if n=='2':
    num2 = input("Type the first observation : ")
    num3 = input("Type the second observation : ")
    mean1 = (float(num2)+float(num3))/2
    print("The arithmetic mean of the given data is = ", '**',mean1,'**')
else:
    print('')
if n=='3':
    num4 = input("Type the first observation : ")
    num5 = input("Type the second observation : ")
    num6 = input("Type the third observation : ")
    mean2 = (float(num4)+float(num5)+float(num6))/3
    print("The arithmetic mean of the given data is = ", '**',mean2,'**')
else:
    print('')
if n=='4':
    num7 = input("Type the first observation : ")
    num8 = input("Type the second observation : ")
    num9 = input("Type the third observation : ")
    num10 = input('Type the fourth observation : ')
    mean4 = (float(num7)+float(num8)+float(num9)+float(num10))/4
    print("The arithmetic mean of the given data is = ", '**',mean4,'**')
else:
    print('')
if n=='5':
    num11 = input("Type the first observation : ")
    num12 = input("Type the second observation : ")
    num13 = input("Type the third observation : ")
    num14 = input('Type the fourth observation : ')
    num15 = input('Type the fifth observation : ')
    mean5 = (float(num11)+float(num12)+float(num13)+float(num14)+float(num15))/5
    print("The arithmetic mean of the given data is = ", '**',mean5,'**')
else:
    print('')
time.sleep(0.2)
print("************")
