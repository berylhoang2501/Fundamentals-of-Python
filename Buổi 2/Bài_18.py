import math 

a,b,c=eval(input('Nhập hệ số a,b,c để giải PTB2: '))

if a == 0:
    if b == 0 and c == 0:
        print('Phương trình có vô số nghiệm')
    elif b==0 and c!=0:
        print('Phương trình vô nghiệm')
    else: 
        # print('Nghiệm của phương trình là x = %1f'%(-b/(2*a)))
        print('Nghiệm x= {:.1f}'.format(-b/2*a))

else:
    delta = b**2-4*a*c
    if delta > 0:  
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(x1)
        print(x2)
        print('Nghiệm của phương trình là x1, x2 = {}, {}'.format(x1,x2))
    elif delta == 0:
        x = -b / (2*a)
        print('Nghiệm kép của phương trình là x1 = x2 = {}'.format(x))
    else:
        print('Phương trình vô nghiệm')
        
#2 dấu % lồng vô nhau để matching với nhau lúc in kết quả