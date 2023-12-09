#Viết chương trình nhập vào một số nguyên, 
# kiếm tra và in ra màn hình đó là số ngueyen dương, nguyên âm hay số 0

so=int(input('Nhập 1 số để kiểm tra: '))
if so>0:
    print(so, 'là só dương')
elif so<0:
    print(so, 'là số âm')
else:
    print('Số 0')
    
