MM = 'mm'
INCHES = 'in'
FORWARD = 'forward'
BACKWARD = 'backward'
REVERSE = 'backward'
LEFT = 'left'
RIGHT = 'right'
DEGREES = 'degrees'

class Robot():
    def main(self):
        exit('Nothing In "Main" function!')
    def run(self):
        self.main()

class Drivetrain():
    def drive_for(self, direction, amount, units):
        if direction == BACKWARD or direction == FORWARD and units == MM or units == INCHES:
            print('Driving ' + direction + ' for ' + str(amount) + units)
        else:
            exit('(Drivetrain_drive_for) Invalid Direction or Units!')
    def drive(self, direction):
        if direction == BACKWARD or direction == FORWARD:
            print('Driving ' + direction)
        else:
            exit('(Drivetrain_drive) Invalid Direction!')
    def stop(self):
        print('Stopping Drivetrain')

class Motor():
    def turn(self, direction):
        if direction == RIGHT or direction == LEFT:
            print('Turning ' + direction)
        else:
            exit('(Motor_turn) Invalid Direction!')
    def turn_for(self, direction, amount, units):
        if direction == LEFT or direction == RIGHT and units == DEGREES:
            print('Turning ' + direction + ' for ' + str(amount) + units)
        else:
            exit('(Motor_turn_for) Invalid Direction or Units!')