a=''
sys=0
print('введите число')
try:
    chislo = int(input())
except ValueError:
        print('ошибка ввода')
else:
    if chislo<0:
        print('ошибка ввода')
        exit()
    else:
        while sys!=8 and sys!=2:
            print('выберете целевую систему счисления: 2 или 8 и напишите цифрой')
            try:
                sys = int(input())
            except ValueError:
                print('ошибка ввода')
            else:
                def dv(x):
                    a=''
                    while x > 0:
                        a = str(x % 2) + a
                        x = x // 2
                    return a
                def vos(x):
                    a=''
                    while x > 0:
                        a = str(x % 8) + a
                        x = x // 8
                    return a
                if sys==2:
                    print('ваше число в двоичной системе счисления:',dv(chislo))
                    
                if sys==8:
                    print('ваше число в восьмиричной системе счисления:', vos(chislo))
                    
                
        


    
