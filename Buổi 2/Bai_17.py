# Viết chương trình gỉai phương trình bậc nhất

a,b=eval(input('Nhập hệ số a,b cuat PTB1: '))

if a == 0 and b == 0:
    print('Phương trình có vô số nghiệm')
elif a == 0 and b != 0:
    print('Phương trình vô nghiệm')
else:
    # print('Nghiem x= %.1f'%(-b/a))
    print('Nghiem x= {:.1f}'.format(-b/a))
    

