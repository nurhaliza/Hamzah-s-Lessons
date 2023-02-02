"""
8. Choji decided to invite his friends over for breakfast. He is making omelets and one omelet
is made with one tomato and two eggs. Choji has 17 tomatoes and 124 eggs. How many 
more tomatoes does he need to make omelets for breakfast? Please write your code in the 
review-6.py in your Week 3 folder. 
"""

# print("Choji needs: " , ((124 / 2) / 2) - 17 ,  "tomatoes to make omelets.") 

# ==== Ngah's Solution ====
# define variables (ingredients)
eggs = 124
tomatoes = 17

# calculations
findtomatoes1 = eggs / 2 # equals 62
findtomatoes2 = findtomatoes1 / 2 # tomatoes total needed for total amount of omelets
findtomatoes3 = findtomatoes2 - 17

# print outcome
print (findtomatoes3)

