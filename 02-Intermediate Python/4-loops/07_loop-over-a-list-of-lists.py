'''
07 - Loop over list of lists

Remember the house variable from the Intro to Python course?
Have a look at its definition on the right. It's basically a list of lists,
where each sublist contains the name and area of a room in your house.

It's up to you to build a for loop from scratch this time!

Instructions:

 - Write a for loop that goes through each sublist of house and prints out the x is y sqm,
 
 - where x is the name of the room and y is the area of the room.
'''
# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch
for room, area in house :
    print("the " + str(room) + " is " + str(area) + " sqm")
