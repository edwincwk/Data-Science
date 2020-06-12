import numpy as np
import matplotlib.pyplot as plt
F = 'File Path/folder path/hdb-resident-population.csv'
File = np.loadtxt(F,delimiter=',', skiprows=1, dtype=[('shs_year','i4'),('hdb_resident_population','i8')])
shs_year = File['shs_year']
hdb_resident_population = File['hdb_resident_population']

plt.figure(figsize=(10,5))
plt.plot(shs_year, hdb_resident_population, linewidth=3, c='b')
plt.xlim(1985,2015)
plt.ylim(2200000,3100000)
plt.xlabel('Year', c='b', fontsize=13)
plt.ylabel('HDB Resident Population', c='b', fontsize=13)
plt.suptitle('HDB Resident Population from 1987 to 2013',fontsize=15,fontweight='bold')
plt.show()


