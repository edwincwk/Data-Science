import numpy as np
F = "File Path/folder path/number-of-resale-applications-registered-by-flat-type.csv"
File = np.loadtxt(F,delimiter=',', skiprows=1,
             dtype=[('quarter','U10'),('flat_type','U10'),('no_of_resale_applications','i8')])

Filename = "Number of resale flat applications from 2007 to 2019 by quarterly"
quarter = set(File['quarter'])
flat_type = set(File['flat_type'])
resaleapp = set(File['no_of_resale_applications'])
min_row = np.argmin(File['no_of_resale_applications'])
max_row = np.argmax(File['no_of_resale_applications'])
var = np.var(File['no_of_resale_applications'])
std = np.std(File['no_of_resale_applications'])
med = np.median(File['no_of_resale_applications'])
mean = np.mean(File['no_of_resale_applications'])

print("\n***{}***\n".format(Filename))
print("There are {} rows and {} columns in this dataset.".format(len(File),(len(File[0]))))
print("There are {} unique values in quarter column.".format(str(len(quarter))))
print("There are {} unique values in flat type column.".format(str(len(flat_type))))
print("There are {} unique values in number of resale applications column.".format(str(len(resaleapp))))
print('The mean number of resale flat applications from 2007 to 2019 is {:.0f}.'.format(mean))
print('The median number of resale flat applications from 2007 to 2019 is {:.0f}.'.format(med))
print('The standard deviation of resale flat applications from 2007 to 2019 is {:.0f}.'.format(std))
print("The minimum number of resale application is a {} flat, with a total of {} application during the year-quarter {}.".format(File[min_row][1],
      File[min_row][2],File[min_row][0]))
print("The maximum number of resale applications is a {} flat, with a total of {} applications during the year-quarter {}.".format(File[max_row][1],
      File[max_row][2], File[max_row][0] ))
