#PART A
import ast
origin = ast.literal_eval(input("Enter the origin coordinates (x1,y1): ")) #lets the user input the origin coordinates.
destination = ast.literal_eval(input("Enter the destination coordinates (x2,y2): ")) #lets the user input the destination coordinates.
(x1,y1) = origin #origin coordinates
(x2,y2) = destination #destinaion coordinates
distance = pow(( x2-x1)**2 + (y2-y1)**2, 0.5)  #distance formula
print("Distance to destination: ", distance , "metres") #prints the distance to reach the destination, on the terminal.

#PART B
initialvelocity = float(input("Initial velocity :")) #lets the user input the value of initial velocity
acceleration = float(input("acceleration :")) #lets the user input the value of acceleration
topspeed = float(input("Maximum allowed top speed :")) #lets the user input the value of maximum allowed top speed
if(acceleration ==0):
    t1 = 0  #PART C = error handling, since division by zero not possible while calculating t1
else:
    t1 = ((topspeed - initialvelocity)/ acceleration ) # time taken to reach the maximum top speed
d1 = (initialvelocity*t1) + (0.5*acceleration*t1**2) # distance covered during the time of acceleration
d2 = distance - d1 #distance covered during the time of constant speed(top speed)
t2 = d2/topspeed # time taken to cover d2
time = t1+t2 #total time
print("Time Required :", time, "seconds") #prints the time required, on the terminal