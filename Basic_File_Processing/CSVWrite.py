f=open('City.csv','w')

ls=[
    ['City','Floor Price (¥/square)','Premium Rate (%)','Land Conveyance Fees (BN¥)'],
    ['Hangzhou','8149','27.23','250'],
    ['Shanghai','8328','0.83','182'],
    ['Beijing','19751','14.01','159'],
    ['Guangzhou','6093','7.17','140'],
    ]

for row in ls:
    f.write(','.join(row)+'\n')
f.close()
