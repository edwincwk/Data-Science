import numpy as np
import matplotlib.pyplot as plt
F = 'File Path/folder path/demand-for-rental-and-sold-flats.csv'
File = np.loadtxt(F,delimiter=',', skiprows=1, 
                  dtype=[('start_year','i4'), ('end_year','i4'), ('flat_type', 'U40'),('demand_for_flats','i8')])
             
x_rental = File[File['flat_type']=='rental_flats']['demand_for_flats']
y_rental = File[File['flat_type']=='rental_flats']['start_year']
x_home = File[File['flat_type']=='home_ownership_flats']['demand_for_flats']
y_home = File[File['flat_type']=='home_ownership_flats']['start_year']

fig = plt.figure(figsize=(12,6))
fig.suptitle('Demand for Rental flats vs Owned flats',fontsize=17, fontweight='bold')
plt1 = fig.add_subplot(111)
plt1.scatter(x_rental, y_rental, c='g', s=50, marker='o', label='Rental Flats')
plt1.scatter(x_home, y_home, c='r', s=50, marker='*', label='Home Ownership Flats')
plt.legend(loc='upper right', prop={'size': 15});
plt.ylabel('Year', c='b', fontsize=15)
plt.xlabel('Number of demand for flats', c='b', fontsize=15)
plt.ylim(1955,2020)
plt.xlim(0,350000)
plt.show()




