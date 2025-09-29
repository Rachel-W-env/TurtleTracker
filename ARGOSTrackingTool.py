#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Rachel Williams (rachel.williams@duke.edu)
# Date:   Fall 2025
#--------------------------------------------------------------
# Parse Data
# Copy and paste a line of data as the lineString variable value
lineString = "20640	29051	7/4/2003 3:42	B	0	34.136	-77.725	31.25	-91.766	2	0	-126	53	2	401 651179.0	0"
  
# Use the split command to parse the items in lineString into a list object
lineData = lineString.split()
  
# Assign variables to specfic items in the list
record_id = lineData[1]   # ARGOS tracking record ID
obs_date = lineData[2]   # Observation date
ob_lc = lineData[3]       # Observation Location Class
obs_lat = lineData[5]     # Observation Latitude
obs_lon = lineData[6]     # Observation Longitude
  
# Print information to the use
print (f"Record {record_id} indicates Sara was seen at {obs_lat}N and {obs_lon}W on {obs_date}")