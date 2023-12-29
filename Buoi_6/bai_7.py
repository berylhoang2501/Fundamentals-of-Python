from functools import reduce
list_so=[-1,98,27,17,6,9,12,5,16,27]
list_gap_doi=list(map(lambda x:x*2,list_so))
print('List các phần tử có vị trí gấp đôi: ',list_gap_doi)

def check_prime(so):
    if so<2:
        return False
    else:
        for i in range(2,so):
            if so%i==0:
                return False
        else: 
            return True
list_songuyento=list(filter(check_prime,list_so))
print('List các số nguyên tố: ',list_songuyento)
tinh_tich=lambda x,y:x*y
tich=reduce(tinh_tich,list_so)
print('Tích của các phần tử: ',tich)
