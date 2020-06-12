import numpy as np
F = "File Path/folder path/demand-for-rental-and-sold-flats.csv"
File = np.loadtxt(F,delimiter=',', skiprows=1,
             dtype=[('start_year','i4'),('end_year','i4'), ('flat_type', 'U40'),('demand_for_flats','i8')])

Filename = 'Demand for rental and sold flats from 1960 to 2017'
start_year = set(File['start_year'])
end_year = set(File['end_year'])
flat_type = set(File['flat_type'])
demand_for_flats = set(File['demand_for_flats'])
maximum = np.max(File['demand_for_flats'])
minimum = np.min(File['demand_for_flats'])           
max_row = np.argmax(File['demand_for_flats'])
min_row = np.argmin(File['demand_for_flats'])
var = np.var(File['demand_for_flats'])
std = np.std(File['demand_for_flats'])
med = np.median(File['demand_for_flats'])
mean = np.mean(File['demand_for_flats'])

print('\n***{}***\n'.format(Filename))
print('There are {} rows and {} columns in this dataset.'.format(len(File), len(File[0])))
print('There are ' + str(len(start_year)) + ' unique values in start year column.')
print('There are ' + str(len(end_year)) + ' unique values in end year column.')
print('There are ' + str(len(flat_type)) + ' unique values in flat type column.')
print('There are ' + str(len(demand_for_flats)) + ' unique values in demand for flats column.')
print('The mean number of demand for flats from 1960 to 2017 is {:.0f}.'.format(mean))
print('The median number of demand for flats from 1960 to 2017 is {:.0f}.'.format(med))
print('The standard deviation of demand for flats from 1960 to 2017 flats is {:.0f}.'.format(std))
print('The minimum number of demand for flats is from {} to {}, with a total demand of {} and under the category {}.'
      .format(File[min_row][0],File[min_row][1],File[min_row][3],File[min_row][2]))
print('The maximum number of demand for flats is from {} to {}, with a total demand of {} and under the category {}.'
      .format(File[max_row][0],File[max_row][1],File[max_row][3],File[max_row][2]))
