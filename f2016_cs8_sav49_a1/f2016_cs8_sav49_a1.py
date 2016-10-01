##############################################
# name  : Sandiya Venkatesh
# email : SAV49@pitt.edu
# date  : Sep 30 2016
# class : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
##############################################
# Description:
# CS 0008 - Fall 2016 / Assignment #1
# Notes:
###############################################

# PROGRAM START ###############################

# User input
system_used = input('Enter your preferred system, USC or METRIC : ')

# Check to make sure that user entered, USC or METRIC
while not (system_used == 'USC' or system_used == 'METRIC'):
    print('Invalid system entered')
    system_used = input('Enter your preferred system, USC or METRIC : ')

# User input miles/gallons and convert to KM/liters
if system_used == 'USC':
    dis_driven_miles = float(input('Enter distance driven : '))
    gas_used_gal = float(input('Enter gasoline used : '))

    dis_driven_km = dis_driven_miles * 1.60934
    gas_used_liters = gas_used_gal * 3.78541

# User input KM/liters  and convert to miles/gallons
else:
    dis_driven_km = float(input('Enter distance driven : '))
    gas_used_liters = float(input('Enter gasoline used : '))

    dis_driven_miles = dis_driven_km * 0.621371
    gas_used_gal = gas_used_liters * 0.264172

# Gas consumption calculation
miles_per_gal = dis_driven_miles / gas_used_gal
liters_per_100_km = 100 * gas_used_liters / dis_driven_km

# Rating calculation
if liters_per_100_km <= 8:
    rating = 'Excellent'
elif liters_per_100_km > 8 and liters_per_100_km <= 10:
    rating = 'Good'
elif liters_per_100_km > 10 and liters_per_100_km <= 15:
    rating = 'Average'
elif liters_per_100_km > 15 and liters_per_100_km <= 20:
    rating = 'Poor'
elif liters_per_100_km > 20:
    rating = 'Extremely Poor'
else:
    print('Invalid liters_per_100_km :', liters_per_100_km)

# Formatting output
dis_driven_km = format(dis_driven_km, '12.3f')
gas_used_liters = format(gas_used_liters, '12.3f')
dis_driven_miles = format(dis_driven_miles, '12.3f')
gas_used_gal = format(gas_used_gal, '12.3f')
miles_per_gal = format(miles_per_gal, '12.3f')
liters_per_100_km = format(liters_per_100_km, '12.3f')

# Final output
print('{:>40}'.format('USC'), '{:>19}'.format('Metric'))
print('Distance_______________:', dis_driven_miles, 'miles    ', dis_driven_km, 'Km')
print('Gas____________________:', gas_used_gal, 'gallons  ', gas_used_liters, 'Liters')
print('Consumption____________:', miles_per_gal, 'mpg      ', liters_per_100_km, '1\\100Km')
print('\n')
print('Gas Consumption Rating :', rating)

# PROGRAM END ##################################

