import math 
""" ==============================================================================
For the following problems you must abide by this note. NOTE: You may not use one 
print statement for your entire solution. You must implement the solution in the way 
we have reviewed. Please write your code in review-9.py in your Week 4 folder. 
============================================================================== """ 

"""
4. Drake decided to buy a bunch of marbles. He bought 985482 marbles and needed to put them 
into bags. Drake only has 97 bags. How many marbles can Drake put in each bag? 
"""
# big brain solution

# define how many bags and marbles does drake has
bags = 97
marbles = 985482.0

# define math = division problem
totalbags = marbles / bags
updatedvalue = math.trunc(totalbags)

# number sentence
print("Drake needs to put in: ",(updatedvalue), ", marbles in each bag.")


"""
5.  a. Kazekage Gaara must dispatch an order of 50070 pieces of cotton for each shinobi's 
outfit for war. The Sand Village already has 19832 pieces of cotton. How much more does 
the Sand Village need?

    b. The villagers in charge of making the clothes for the shinobi have determined that
    each outfit requires 7 pieces of cotton. How many outfits can the villagers make in total?
"""
# big brain solution

# define a, pieces of cotton.
order_of_cottons = 50070
cottons_already_have = 19832

# define math's big bing chilling brain = subtraction problem
total_cottons_they_need = order_of_cottons - cottons_already_have 

# print statement
print("Lord Gaara needs: ",(total_cottons_they_need), "cottons in preparations of the fourth great ninja war.")


# not all, gotta solve for b too.
cottons_already_have = 19832
requires_each_cotton = 7

# define math, smarty pants = divison problem
requirescotton = cottons_already_have / requires_each_cotton
updatedvalue = math.trunc(requirescotton)

# print statement
print("The villagers of the Hidden Sand will require: ",(updatedvalue), "cottons for the shinobi of the hidden sand.")



# 6. Write a program that gives us the instructions for making Buldak Noodles.
# big brain solution

# ingredients and first step
step = "1. Use a pot and fill it up with water and turn on the heat and let it sit until it starts boiling."
ingredients = "noodles, buldak sauce, and cheese(for the people that likes cheese with the noodles on it.)"

# first bing chilling output baby
print("Before I could make Buldak noodles, i must collect the following: \n" + ingredients)
print("Now that I have collected the ingredients for making Buldak noodles, the steps are as follows: \n" + step)

# second bing chilling output baby
step = "2. When the water is boiling, put the noodles in and let it sit there for about 3-4 minutes."
print(step)

# third bing chilling output baby
step = "3. Take the water out in the sink and do not let the noodles slip in the sink!"
print(step)

# tip bing chilling output baby
step = "TIP: For the people that can't take the spice of the buldak noodles, if you have cheese in your refridgerator, take it out and sprinkle the cheese on the noodles."
print(step)

# fourth bing chilling output baby
step = "4. Warm the buldak noodles for about a minute and a half."
print(step)

# tip number two bing chilling output baby
step = "TIP 2: While the noodles are warming up, add some side dishes like any korean dishes. My recommendations for eating buldak noodles and a side dish would be kimchi."
print(step)

# fifth bing chilling output baby
step = "5. After it is done warming up the noodles for about a minute and a half, take it out and... TA-DAAAA, you have officially made your own Buldak Noodles with my instructions, you must be hungry now, go ahead and eat and I shall see you next time! Good Night!"
print(step)

# coding python is O.P (overpowered) and the G.O.A.T (greatest of all time)
