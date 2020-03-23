# Universal Gravity Calculator (12pts)
# In physics, the force of gravity between two objects can be calculated using the equation:
# F = G * (m1 * m2) / r**2
# F is the force of gravity in Newtons
# G is the universal gravity constant (6.67e-11)
# m1 is the mass of first object in kg
# m2 is the mass of the second object in kg
# r is the center to center distance between the objects in meters

done = False

# Make a calculator that does all of the following
# (3pts) takes the inputs for mass 1, mass 2, and distance between the two objects (m1, m2, and r)
y = 2
done = False
G = 6.7e-11
while not done:
     try:
         m1 = input("Insert Mass 1 ...")
         m1 = int(m1)
         m2 = input("Insert Mass 2 ...")
         m2 = int(m2)
         r = input("Insert Radius ...")
         r = int(r)
         F = G * (m1 * m2) / r ** 2
         print(F)
         done = True

     except:
         print("Invalid, reinsert values ...")


# (4pts) contains exceptions for any potential errors (value and dividebyzero).
# (2pts) keeps asking for inputs until they are valid (see while loop from notes)
# (3pts) calculates the force of gravity in Newtons and print the result to the user in scientific notation to two decimals.





