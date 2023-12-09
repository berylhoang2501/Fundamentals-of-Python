so_kwh=int(input('Nhập số kwh: '))

if so_kwh <= 50:
    tien_dien = so_kwh * 1678
elif so_kwh <= 100:
    tien_dien = 50 * 1678 + ((so_kwh - 50) * 1734)
elif so_kwh <= 200:
    tien_dien = 50 * 1678 + 50 * 1734 + ((so_kwh - 100) * 2014)
elif so_kwh <= 300:
    tien_dien = 50 * 1678 + 50 * 1734 + 100 * 2014 + ((so_kwh-200) * 2536)
elif so_kwh <= 400:   
    tien_dien = 50 * 1678 + 50 * 1734 + 100 * 2014 + 100 * 2536 + ((so_kwh - 300) * 2834)
else:
    tien_dien = 50 * 1678 + 50 * 1734 + 100 * 2014 + 100 * 2536 + 100 * 2843 + ((so_kwh - 400) * 2927)

print('Số tiền điện cần phải trả:', tien_dien)
    
  
