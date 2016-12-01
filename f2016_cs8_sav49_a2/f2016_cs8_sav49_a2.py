##############################################
# name  : Sandiya Venkatesh
# email : SAV49@pitt.edu
# date  : Oct 28 2016
# class : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
##############################################
# Description:
# CS 0008 - Fall 2016 / Assignment #2
# Notes:
###############################################

# PROGRAM START ###############################

###############################################
# FUNCTION DEFINITION #########################
###############################################

# Begin processFile() function
def processFile(fh):
    # Initialize a variable for tracking file line count
    file_line_count = 0

    # Initialize a variable for accumulating distance count
    file_distance_total = 0.0

    # Open file for reading.
    fetch_file = open(fh, 'r')

    # Read all lines from the file.
    for line in fetch_file:
        # Increase file count by 1
        file_line_count += 1

        # Remove /n (new line character)
        line = line.rstrip('/n')

        # Split comma separated line content
        distance = line.split(',')

        # Calculate total distance
        file_distance_total += float(distance[1])

    # close file
    fetch_file.close()

    # Return file line count and total distance value
    return file_line_count, file_distance_total


# End processFile() function

# Begin printKV() function
def printKV(key, value, klen=0):
    # print left justified key
    print(key.ljust(klen), ':', value)


# End printKV() function

###############################################
# MAIN PROGRAM ################################
###############################################

# Initialize a variable for finding cumulative line count
g_cumulative_file_line_count = 0

# Initialize a variable for finding cumulative distance count
g_cumulative_file_distance_total = 0

# Create a variable to fetch file name.
g_file = input('File to be read : ')

# Do the loop until user enters quit
# MN: you are missing the option when the user just hits enter
#while not (g_file.lower() == 'q' or g_file.lower() == 'quit'):
while not (g_file == '' or g_file.lower() == 'q' or g_file.lower() == 'quit'):
    # call processFile() function
    g_file_line_count, g_file_distance_total = processFile(g_file)

    # call printKV() function
    printKV('Partial Total # of Lines', g_file_line_count, 30)
    printKV('Partial Distance Run', format(g_file_distance_total, '.3f'), 30)
    print()

    # Calculate cumulative line count and distance count
    g_cumulative_file_line_count += g_file_line_count
    g_cumulative_file_distance_total += g_file_distance_total

    # Fetch the next file name or exit from the program.
    g_file = input('File to be read : ')

# Print cumulative line count and distance count
print()
print('Totals')
printKV('Total # of Lines', g_cumulative_file_line_count, 30)
printKV('Total Distance Run', format(g_cumulative_file_distance_total, '.3f'), 30)

# PROGRAM END #################################






