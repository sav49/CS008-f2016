##############################################
# name  : Sandiya Venkatesh
# email : SAV49@pitt.edu
# date  : Nov 18 2016
# class : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
##############################################
# Description:
# CS 0008 - Fall 2016 / Assignment #3
# Notes:
# MN: creating the output file is missing
# 
###############################################

###############################################
# FUNCTION DEFINITION #########################
###############################################


# Begin processFile() function
def processFile(fh):
    # Initialize a list to store file contents
    temp_file_list = []

    # Initialize a variable for tracking file line count
    file_line_count = 0

    # Initialize a variable for accumulating distance count
    file_distance_total = 0.0

    # Initialize a variable for capturing max distance and participant name
    file_max_distance = 0.0
    file_max_name = ''

    # Initialize a variable for capturing min distance and participant name
    file_min_distance = 0.0
    file_min_name = ''

    # Open file for reading.
    fetch_file = open(fh, 'r')

    # Read all lines from the file.
    for line in fetch_file:

        # Remove /n (new line character)
        line = line.rstrip('\n')

        # Split comma separated line content
        distance = line.split(',')

        # Check wheather distance[1] has float value
        # if isinstance(distance[1],float):
        if distance[1].lower() != 'distance':

            # Calculate total distance
            file_distance_total += float(distance[1])

            # Add line into list
            temp_file_list.append(line.split(','))

            # MN: here you compute min and max on each single run and not on the total distance run by the participant
            # Capture max distance
            if float(distance[1]) > file_max_distance:
                file_max_distance = float(distance[1])
                file_max_name = distance[0]

            # Capture min distance
            if (file_min_distance == 0.0) or (float(distance[1]) < file_min_distance):
                file_min_distance = float(distance[1])
                file_min_name = distance[0]

            # Increae file count by 1
            file_line_count += 1

    # close file
    fetch_file.close()

    # Return temporary file list, file line count and total distance value
    return temp_file_list, file_line_count, file_distance_total, file_max_distance, file_max_name, file_min_distance, file_min_name

    # MN: you need to move this statement right before the return , otheriwse is never executed
    # close file
    #fetch_file.close()


# End processFile() function

# Begin printKV() function
def printKV(key, value, klen=0):
    # print left justified key
    print(key.ljust(klen), ':', value)


# End printKV() function

###############################################
# MAIN PROGRAM ################################
###############################################

# Initialize a variable for storing file count
g_file_count = 0

# Initialize a global list to store all file contents
g_cumulative_file_list = []
g_temp_file_list = []

# Initialize a variable for finding cumulative line count
g_cumulative_file_line_count = 0
g_temp_line_count = 0

# Initialize a variable for finding cumulative distance count
g_cumulative_file_distance_total = 0.0
g_temp_distance_total = 0.0

# Initialize a variable for capturing max distance and participant name
g_file_max_distance = 0.0
g_temp_file_max_distance = 0.0
g_file_max_name = ''
g_temp_file_max_name = ''

# Initialize a variable for capturing min distance and participant name
g_file_min_distance = 0.0
g_temp_file_min_distance = 0.0
g_file_min_name = ''
g_temp_file_min_name = ''

# Open master file to read file content
master_file = open('f2016_cs8_a3.data.txt', 'r')

# Read all lines from the master_file
for line in master_file:

    # Increae file count by 1
    g_file_count += 1

    # Remove /n (new line character)
    line = line.rstrip('\n')

    # Get the file name from master file and pass the file name to processFile() function
    # Store the return from processFile() into g_temp_file_list, g_temp_line_count, g_temp_distance_total
    g_temp_file_list, g_temp_line_count, g_temp_distance_total, g_temp_file_max_distance, g_temp_file_max_name, g_temp_file_min_distance, g_temp_file_min_name = processFile(
        line)

    # Store values in g_temp_file_list to g_file_list
    g_cumulative_file_list += g_temp_file_list

    # Store the value from g_temp_line_count to g_cumulative_file_line_count
    g_cumulative_file_line_count += g_temp_line_count

    # Store the value from g_temp_distance_total to g_cumulative_file_distance_total
    g_cumulative_file_distance_total += g_temp_distance_total

    # Find out max distance
    if float(g_temp_file_max_distance) > g_file_max_distance:
        g_file_max_distance = float(g_temp_file_max_distance)
        g_file_max_name = g_temp_file_max_name

    # Find out min distance
    if (g_file_min_distance == 0.0) or (float(g_temp_file_min_distance) < g_file_min_distance):
        g_file_min_distance = float(g_temp_file_min_distance)
        g_file_min_name = g_temp_file_min_name

# close master_file
master_file.close()

# unique participants
unique_participants = []
mutiple_occurence_participants = []
for row in g_cumulative_file_list:
    if row[0] not in unique_participants:
        unique_participants.append(row[0])
    else:
        mutiple_occurence_participants.append(row[0])

# print results
printKV('Number of Input files read', g_file_count, 50)
printKV('Total number of lines read', g_cumulative_file_line_count, 50)
print()
printKV('Total distance run', format(g_cumulative_file_distance_total, '.5f'), 50)
print()

printKV('max distance run', format(g_file_max_distance, '.5f'), 50)
printKV('by participant', g_file_max_name, 50)
print()

printKV('min distance run', format(g_file_min_distance, '.5f'), 50)
printKV('by participant', g_file_min_name, 50)
print()

printKV('Total number of participants', len(unique_participants), 50)
printKV('Number of participants with multiple records', len(mutiple_occurence_participants), 50)



# PROGRAM END #################################

