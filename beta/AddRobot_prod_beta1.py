# What problem are we solving here:
# 1. Located the directry where robots files are stored in your local machine
# 2. Successfully add the robot without accessing the online library
# 4. Add the robot to the active station.

from robodk.robolink import *  # API to communicate with RoboDK
from robodk.robodialogs import *
from robodk.robofileio import *

#----------------------------
# Global variables:

# Set the name of the reference target
# (orientation will be kept constant with respect to this target)
TARGET_NAME = 'Home'

#---------------------------
# Start the RoboDK API
RDK = Robolink()

# Ask the user to pick a file:
rdk_file_path = RDK.getParam("PATH_OPENSTATION")

path_file = getOpenFile(rdk_file_path + "/")
if not path_file:
    print("Nothing is selected")
    quit()

# Open and add the file to the active station
RDK.AddFile(path_file)

RDK.ShowMessage("Done", False)
print("Done")

