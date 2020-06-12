import numpy as np
F = "C:/Users/User/Desktop/suss/specialised dip/Introduction to programming for DS/assignment excel/resale-flat-prices-based-on-registration-date-from-jan-2017-onwards.csv"
File = np.loadtxt(F,delimiter=',', skiprows=1,
             dtype=[('month','U10'),('town','U40'), ('flat_type', 'U10'),('block','U6'),('street_name', 'U40'),('storey_range', 'U10'),
                    ('floor_area','i4'),('flat_mode','U40'),('lease_commence_date','i4'),('remaining_lease','U20'),('resale_price','f8')])

Filename = 'Resale Flat Prices from 2017 to 2019'
month = set(File['month'])
town = set(File['town'])
flat_type = set(File['flat_type'])
block = set(File['block'])
street_name = set(File['street_name'])
storey_range = set(File['storey_range'])
floor_area = set(File['floor_area'])
flat_mode = set(File['flat_mode'])
lease_commence_date = set(File['lease_commence_date'])
remaining_lease = set(File['remaining_lease'])
resale_price = set(File['resale_price'])
min_row = np.argmin(File['resale_price'])
max_row = np.argmax(File['resale_price'])
var = np.var(File['resale_price'])
std = np.std(File['resale_price'])
med = np.median(File['resale_price'])
mean = np.mean(File['resale_price'])

print('\n***{}***\n'.format(Filename))
print("There are {} rows and {} columns in this dataset.".format(len(File),(len(File[0]))))
print("There are {} unique values in month column.".format(str(len(month))))
print("There are {} unique values in town column.".format(str(len(town))))
print("There are {} unique values in flat type column.".format(str(len(flat_type))))
print("There are {} unique values in block column.".format(str(len(block))))        
print("There are {} unique values in street name column.".format(str(len(street_name))))
print("There are {} unique values in storey range.".format(str(len(storey_range))))
print("There are {} unique values in floor area column.".format(str(len(floor_area))))
print("There are {} unique values in flat mode column.".format(str(len(flat_mode))))
print("There are {} unique values in lease commence date column.".format(str(len(lease_commence_date))))        
print("There are {} unique values in remaining lease column.".format(str(len(remaining_lease))))
print("There are {} unique values in resale price column.".format(str(len(resale_price))))
print('The mean resale flat prices from 2017 to 2019 is {:.0f}.'.format(mean))
print('The median resale flat prices from 2017 to 2019 is {:.0f}.'.format(med))
print('The standard deviation for resale flat prices from 2017 to 2019 is is {:.0f}.'.format(std))
print("The minimum resale price of {:.0f} is a {}, {} flat and in the town area of {} during the year-quarter {}.".format(
        File[min_row][10],File[min_row][2],File[min_row][7],File[min_row][1], File[min_row][0] ))
print("The maximum resale price of {:.0f} is a {}, {} flat and in the town area of {} during the year-quarter {}.".format(
        File[max_row][10],File[max_row][2],File[max_row][7],File[max_row][1], File[max_row][0] ))