# What problem are we solving here:
# 1. Located the directry where robots files are stored in your local machine
# 2. Successfully add the robot without accessing the online library
# 4. Add the robot to the active station.

from robodk.robolink import *  # API to communicate with RoboDK
from robodk.robodialogs import *
from robodk.robofileio import *

# ----------------------------
# Global variables:

# LOAD_AS_PROGRAM flag:
# Set to True to generate a program in the UI: we can modify targets manually and properly see the program
# Set to False, it will simulate or generate the robot program directly when running the macro
# LOAD_AS_PROGRAM = True

# Set the name of the reference frame to place the targets:
# REFERENCE_NAME = 'Reference Robot'

# Set the name of the reference target
# (orientation will be kept constant with respect to this target)
TARGET_NAME = "Home"

# ---------------------------
# Start the RoboDK API
RDK = Robolink()

# Ask the user to pick a file:
rdk_file_path = RDK.getParam("PATH_OPENSTATION")

path_file = getOpenFile(rdk_file_path + "/")
if not path_file:
    print("Nothing selected")
    quit()

# Get the program name from the file path
# program_name = getFileName(path_file)

# Open and add the file to the active station
RDK.AddFile(path_file)

RDK.ShowMessage("Done", False)
print("Done")
