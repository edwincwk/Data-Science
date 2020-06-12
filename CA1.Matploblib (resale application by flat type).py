import numpy as np
import matplotlib.pyplot as plt
F = 'C:/Users/User/Desktop/suss/specialised dip/Introduction to programming for DS/assignment excel/number-of-resale-applications-registered-by-flat-type.csv'
File = np.loadtxt(F,delimiter=',', skiprows=1,
             dtype=[('quarter','U10'),('flat_type','U10'),('no_of_resale_applications','i8')])

xlabel = ('Number of quarters from 2007 Q1\nPeriod from 2007-Q1 to 2019-Q3')
ylabel = ('Number of resale applications')
label = set(File['flat_type'])
flatlabel = np.arange(0, len(label))
type_resale = File[['flat_type', 'no_of_resale_applications']]
resaleapp = type_resale['no_of_resale_applications']

while True:
    flattype = 'Option:\n(1) 1-room\n(2) 2-room\n(3) 3-room\n(4) 4-room\n(5) 5-room\n(6) Executive\n(7) End program\nEnter the flat types or end program:'
    flat_type = int(input(flattype))
    flat = ''
    if flat_type == 1:
        value = resaleapp[type_resale['flat_type'] == '1-room']   
        flat = '1-room'
    elif flat_type == 2:
        value = resaleapp[type_resale['flat_type'] == '2-room']   
        flat = '2-room'
    elif flat_type == 3:
        value = resaleapp[type_resale['flat_type'] == '3-room']    
        flat = "3-room"
    elif flat_type == 4:
        value = resaleapp[type_resale['flat_type'] == '4-room']   
        flat = "4-room"
    elif flat_type == 5:
        value = resaleapp[type_resale['flat_type'] == '5-room']    
        flat = "5-room"
    elif flat_type == 6:
        value = resaleapp[type_resale['flat_type'] == 'Executive']   
        flat = 'Executive'
    elif flat_type == 7:
        break

    plt.figure(figsize=(10,5))  
    plt.bar(np.arange(len(value)), value, color='r')
    plt.xlabel(xlabel, color='r', fontsize=13)
    plt.ylabel(ylabel, color='r', fontsize=13)
    plt.title(flat, fontsize=15, fontweight='bold')
    plt.show()

    
