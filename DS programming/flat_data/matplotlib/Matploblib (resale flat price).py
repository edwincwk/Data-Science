import numpy as np
import matplotlib.pyplot as plt
F = 'File Path/folder path/resale-flat-prices-based-on-registration-date-from-jan-2017-onwards.csv'
File = np.loadtxt(F, delimiter=',', skiprows=1,
             dtype=[('month','U10'),('town','U40'), ('flat_type', 'U20'),('block','U6'),('street_name', 'U40'),('storey_range', 'U10'),
                    ('floor_area','i4'),('flat_mode','U40'),('lease_commence_date','i4'),('remaining_lease','U20'),('resale_price','f8')])

label = set(File['flat_type'])
flat_label = ['1 ROOM','2 ROOM','3 ROOM','4 ROOM','5 ROOM','EXECUTIVE', 'MULTI-GENERATION']
type_price = File[['flat_type','resale_price']]
price = type_price['resale_price']
price_1room = price[type_price['flat_type'] == '1 ROOM']
price_2room = price[type_price['flat_type'] == '2 ROOM']
price_3room = price[type_price['flat_type'] == '3 ROOM']
price_4room = price[type_price['flat_type'] == '4 ROOM']
price_5room = price[type_price['flat_type'] == '5 ROOM']
price_executive = price[type_price['flat_type'] == 'EXECUTIVE']
price_multigen = price[type_price['flat_type'] == 'MULTI-GENERATION']
price_alltypes =[price_1room, price_2room, price_3room, price_4room,
                  price_5room, price_executive, price_multigen]

plt.figure(1,figsize=(15,10))
plt.title('Comparison of resale price by different flat types', fontsize=20, fontweight='bold')
plt.ylim(0,12000)
plt.xlabel('Resale Price', fontsize=18)
plt.ylabel('Number of units',fontsize=18)
hist_all = plt.hist(price_alltypes, color=['b','g','r','c','m','y','k'], label=flat_label)

plt.legend()

plt.figure(2,figsize=(10,5)) 
plt.hist(price_1room, color='b', alpha=0.75)
plt.title('1 room',fontsize=15,fontweight='bold')
plt.xlabel('Resale Price',color='b',fontsize=13)
plt.ylabel('Number of units',color='b',fontsize=13)

plt.figure(3,figsize=(10,5)) 
plt.hist(price_2room, color='g',alpha=0.75)
plt.title('2 room',fontsize=15,fontweight='bold')
plt.xlabel('Resale Price',color='g',fontsize=13)
plt.ylabel('Number of units',color='g',fontsize=13)

plt.figure(4,figsize=(10,5)) 
plt.hist(price_3room, color='r',alpha=0.75)
plt.title('3 room',fontsize=15,fontweight='bold')
plt.xlabel('Resale Price',color='r',fontsize=13)
plt.ylabel('Number of units',color='r',fontsize=13)

plt.figure(5,figsize=(10,5)) 
plt.hist(price_4room, color='c',alpha=0.75)
plt.title('4 room',fontsize=15,fontweight='bold')
plt.xlabel('Resale Price',color='c',fontsize=13)
plt.ylabel('Number of units',color='c',fontsize=13)

plt.figure(6,figsize=(10,5)) 
plt.hist(price_5room, color='m',alpha=0.75)
plt.title('5 room',fontsize=15,fontweight='bold')
plt.xlabel('Resale Price',color='m',fontsize=13)
plt.ylabel('Number of units',color='m',fontsize=13)

plt.figure(7,figsize=(10,5)) 
plt.hist(price_executive, color='y',alpha=0.75)
plt.title('Executive',fontsize=15,fontweight='bold')
plt.xlabel('Resale Price',color='y',fontsize=13)
plt.ylabel('Number of units',color='y',fontsize=13)
plt.xticks(rotation='vertical')

plt.figure(8,figsize=(10,5)) 
plt.hist(price_multigen, color='k',alpha=0.5)
plt.title('Multi-Generation',fontsize=15,fontweight='bold')
plt.xlabel('Resale Price',color='k',fontsize=13)
plt.ylabel('Number of units',color='k',fontsize=13)

plt.show()
