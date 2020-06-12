import numpy as np
F = "File Path/folder path//hdb-resident-population.csv"
File = np.loadtxt(F,delimiter=',', skiprows=1, dtype=[('shs_year','i4'),('hdb_resident_population','i8')])

Filename = 'HDB Resident Population from 1987 to 2013'
shs_year = set(File['shs_year'])
hdb_resident_population = set(File['hdb_resident_population'])
maximum = np.max(File['hdb_resident_population'])
minimum = np.min(File['hdb_resident_population'])           
max_row = np.argmax(File['hdb_resident_population'])
min_row = np.argmin(File['hdb_resident_population'])
var = np.var(File['hdb_resident_population'])
std = np.std(File['hdb_resident_population'])
med = np.median(File['hdb_resident_population'])
mean = np.mean(File['hdb_resident_population'])

print('\n***{}***\n'.format(Filename))
print('There are {} rows and {} columns in this dataset.'.format(len(File), len(File[0])))
print('There are ' + str(len(shs_year)) + ' unique values in year column.')
print('There are ' + str(len(hdb_resident_population )) + ' unique values in hdb resident population column.')
print('The mean number of hdb resident population from 1987 to 2013 is {:.0f}.'.format(mean))
print('The median number of hdb resident population from 1987 to 2013 is {:.0f}.'.format(med))
print('The standard deviation of hdb resident population from 1987 to 2013 is {:.0f}.'.format(std))
print('The minimum number of hdb resident population was in the year {} with {} residents.'.format(File[min_row][0],File[min_row][1]))
print('The maximum number of hdb resident population was in the year {} with {} residents.'.format(File[max_row][0],File[max_row][1]))

