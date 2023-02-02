"""
2)
a. Shikamaru has to go to the store to purchase some items for the class he is going to 
teach. He already has 31 erasers and 651 pencils. Each of his students will need 1 eraser 
and 1 pencil. How many more erasers does Shikamaru need?
"""

#==== Brother's Solution in coding review-7.py ====
# define pencils and erasers
pencils = 651
erasers = 31

#==== Hamzah's Big Brain Time ====
totalerasers = pencils - erasers
print("Shikamaru needs: ", (totalerasers), "erasers for his class.")

# b. Shikamaru has $114. Each eraser costs $0.65, how much does all the erasers he got cost?
#==== Brother's Solution for coding in review-7.py ====

# define the variables of money and each eraser cost
money = 114
erasercost = 0.65
 
totalerasercost = (totalerasers * erasercost) - money
print("Shikamaru bought: " ,(totalerasercost), "erasers for his class")
 
 