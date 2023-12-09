#viết chương trình in ra màn hình trị tuyệt đối của 1 số đc nhập từ bàn phím
so=int(input('Nhập 1 số bất kì: '))
tri_tuyet_doi=so
if so<0:
    tri_tuyet_doi=-so
    
# tri_tuyet_doi=abs(so)

print('|{}|={}'.format(so,tri_tuyet_doi))

