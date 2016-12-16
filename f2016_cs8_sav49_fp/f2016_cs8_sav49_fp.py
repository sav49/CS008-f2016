##############################################
# name  : Sandiya Venkatesh
# email : SAV49@pitt.edu
# date  : Dec 15 2016
# class : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
##############################################
# Description:
# CS 0008 - Fall 2016 / Final Project
# Notes:
###############################################

###############################################
# CLASS DEFINITION #########################
###############################################


# Begin class participant definition
class participant:
    """ participant class"""

    # Properties
    # Name of the participant
    name = "unknown"
    # Total distance run by the participant
    distance = 0.0
    # Total number of runs by the participant
    runs = 0

    # Methods
    # Begin Initializer method
    def __init__(self, name, distance=0.0):
        # set name
        self.name = name
        # set distance if non zero
        if distance > 0.0:
            # set distance
            self.distance = distance
            # set number of runs accordingly
            self.runs = 1
            # end if
    # End def __init__

    # Begin addDistance method
    def addDistance(self, distance):
        if distance > 0.0:
            self.distance += distance
            self.runs += 1
            # end if
    # End def addDistance

    # Return the total distance run computed
    def getDistance(self):
        return self.distance
    # End def getDistance

    # Eeturn the number of runs
    def getRuns(self):
        return self.runs
    # End def getRuns

    # stringify the object
    def __str__(self):
        return \
            "Name : " + format(self.name, '>20s') + \
            ". Distance run : " + format(self.distance, '9.4f') + \
            ". Runs : " + format(self.runs, '4d')
        # end def __init__

    # Convert to csv
    def tocsv(self):
        return ','.join([self.name, str(self.runs), str(self.distance)])
    # End def tocsv
# End class participant


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
        distance  = line.split(',')

        # Check wheather distance[1] has float value
        # if isinstance(distance[1],float):
        if distance[1].lower() != 'distance':

            # Calculate total distance
            file_distance_total += float(distance[1])

            # Add line into list
            temp_file_list.append(line.split(','))

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

    # Return temporary file list, file line count and total distance value
    return temp_file_list, file_line_count, file_distance_total, file_max_distance, file_max_name, file_min_distance, file_min_name

    # close file
    fetch_file.close()

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
master_file = open('f2016_cs8_fp.data.txt', 'r')

# Read all lines from the master_file
for line in master_file:

    # Increae file count by 1
    g_file_count += 1

    # Remove /n (new line character)
    line = line.rstrip('\n')

    # Get the file name from master file and pass the file name to processFile() function
    # Store the return from processFile() into g_temp_file_list, g_temp_line_count, g_temp_distance_total
    g_temp_file_list, g_temp_line_count, g_temp_distance_total, g_temp_file_max_distance, g_temp_file_max_name, g_temp_file_min_distance, g_temp_file_min_name = processFile(line)

    # Store values in g_temp_file_list to g_file_list
    g_cumulative_file_list += g_temp_file_list

    # Store the value from g_temp_line_count to g_cumulative_file_line_count
    g_cumulative_file_line_count += g_temp_line_count

    # Store the value from g_temp_distance_total to g_cumulative_file_distance_total
    g_cumulative_file_distance_total += g_temp_distance_total


# Close master_file
master_file.close()


# Compute distance run for each participant and how many records we have for each one of them
# Dictionary with one element for each participant whose value is
# the list of all the distances found in data for the participant
participants = {}

# Loops on all the records
for item in g_cumulative_file_list:
    # check if the names has already been found previously or if it is new
    # if it is new, initialize elements in the accumulators
    item[0] = item[0].strip(' ')
    if not item[0] in participants.keys():
        participants[item[0]] = participant(item[0])

    # insert distance in the list for this participant
    participants[item[0]].addDistance(float(item[1]))


# Computes the min and max distance run for each participant iterating on all the participants
for name, object in participants.items():

    # Find out max distance
    g_temp_file_max_distance = object.getDistance()
    g_temp_file_max_name = name
    if float(g_temp_file_max_distance) > g_file_max_distance:
        g_file_max_distance = float(g_temp_file_max_distance)
        g_file_max_name = g_temp_file_max_name

    # Find out min distance
    g_temp_file_min_distance = object.getDistance()
    g_temp_file_min_name = name
    if (g_file_min_distance == 0.0) or (float(g_temp_file_min_distance) < g_file_min_distance):
        g_file_min_distance = float(g_temp_file_min_distance)
        g_file_min_name = g_temp_file_min_name


# Initialize varibales to capture unique & mutiple occurence participants
unique_participants = 0
mutiple_occurence_participants = 0

# Compute total number of participant
unique_participants = len(participants);


# Compute total number of participants with more than one record
# extract all the participants that have 2 or more runs
# and count the number of elements in the list with len()
mutiple_occurence_participants = len([1 for item in participants.values() if item.getRuns() > 1])


# Create output file
outputFile = "f2016_cs8_sav49_fp.data.output.csv"
# open file for writing
fh = open(outputFile,'w')
# write header in file
fh.write('name,records,distance\n')
# loop on all the participants
for name, object in participants.items():
    # write line in file
    fh.write(object.tocsv() + '\n')

# Close files
fh.close()

# Print results
printKV('Number of Input files read', g_file_count,50)
printKV('Total number of lines read', g_cumulative_file_line_count,50)
print()
printKV('Total distance run', format(g_cumulative_file_distance_total, '.5f'),50)
print()

printKV('max distance run', format(g_file_max_distance, '.5f'),50)
printKV('by participant', g_file_max_name,50)
print()

printKV('min distance run', format(g_file_min_distance, '.5f'),50)
printKV('by participant', g_file_min_name,50)
print()

printKV('Total number of participants', unique_participants,50)
printKV('Number of participants with multiple records', mutiple_occurence_participants,50)



# PROGRAM END #################################

