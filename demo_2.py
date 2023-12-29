#Cấu trúc lặp for trong trường hợp lặp với số lần biết trước
while True:
    n=int(input('Nhập n để countdown: '))
    if n>0:
        break
    else: 
        print('Số countdown cần >0')
for i in range(n,0,-1): #start_stop_step
    print(i,end=',')