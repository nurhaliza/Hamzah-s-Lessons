import math
""" ===================================================================================
For the following problems you must abide by this note. NOTE: You may not use one print 
statement for your entire solution. You must implement the solution in the way we have 
reviewed. Please write your code in review-10.py in your Week 4 folder. 
=================================================================================== """ 

"""
1. a. Killer Bee is on a mission to collect as much octopus ink he can before the Fourth 
Great Ninja War. He manages to find a place by the ocean that has 840 gallons of ink. 
How many ounces of ink does he find?
"""
# bing chilling time

# define gallons of ink and ounces of ink
gallons_of_ink = 840 
ounces_of_ink_in_each_gallon = 128

#define mathmatician bing chilling boooi
inks_in_each_gallon = gallons_of_ink * ounces_of_ink_in_each_gallon

# define statement bing chilling
print("In 840 gallons of ink that Killer Bee has, each gallon to ounces is 128, so Killer Bee has: ",(inks_in_each_gallon), "ounces of ink in preparation for the upcoming Fourth Great Ninja War.")

"""
b. After figuring out how many ounces of ink he found, Killer Bee needs to package the ink. 
Killer Bee brought tiny bags that each can carry 4 ounces of ink. How many bags is Killer Bee
able to package?
"""
# bing chilling time

# define his total ounces of inks he can carry
# inks_in_each_gallon = 107520
ounces_of_ink_per_bag = 4

# define math bing chilling = division problem
requiresink = inks_in_each_gallon / ounces_of_ink_per_bag
updatedvalue = math.trunc(requiresink)
#
# define statement
print("Killer Bee can only carry: ",(updatedvalue), " bags of ounces of ink.")

"""
c. Killer Bee returns to the Hidden Village in the Clouds with the ink and has to give some 
to a blacksmith. The blacksmith will use the ink for special tools to help Killer Bee in the 
upcoming war. Killer Bee only has 1000 bags of ink left. How much ink did Killer Bee give 
to the blacksmith in terms of gallons?
"""
# bing chilling time
# define inks in each gallons and how much he gave the blacksmith.
ounces_of_ink_in_each_gallons = 128
bags_left = 1000

# define math bing chilling = division problem
ounces_of_ink_in_gallons = bags_left / ounces_of_ink_in_each_gallons
updatedvalue = math.trunc(ounces_of_ink_in_gallons)

# define statement
print("In gallons, Killer Bee gave the blacksmith: ",(updatedvalue), "gallons of ink.")


# 2. Write a program that explains steps on how to make wudu.
# bing chilling time

# tip bing output
step = "TIP: Hi guys, Im back again here to teach you how to make wudu. Now, before you do anything, go use the restroom first."
print(step)

# first chilling output
step = "1. After you have used the restroom, wash your hands and that is the first step of making wudu."
print(step)

# second bing output
step = "2. Wash your elbows three times and it always has to be right elbow first and left elbow last."
print(step)

# third chilling output
step = "3. After you have done washing your elbows three times, wash your face three times."
print(step)

# fourth bing output
step = "4. Then, wash your hair three times going up and down."
print(step)

# fifth chilling output
step = "5. Wash your ears three times."

# sixth bing output
step = "6. After you have done that, then wash your right foot first three times, and your left foot three times after your right foot."
print(step)

# tip chilling output
step = "TIP: Congratulations! You have completed your first wudu with my instructions! Don't make Allah wait so go pray now and I will see you next time, good night!"
print(step)
