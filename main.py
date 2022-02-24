# Import OpenRobot (By Wyatt)
from openrobot import *

# Setup Robot
robot = Robot()
# Setup Drivetrain
drivetrain = Drivetrain()
# Setup Motor
motor = Motor()

# Main Code
def main():
    drivetrain.drive_for(FORWARD, 10, MM)

# Run Code (There Are Two Ways Of Doing This)
# Way #1 (This will set the main function, then run it)
robot.main = main
robot.run()
# Way #2 (This will run the main function)
#robot.run(main)