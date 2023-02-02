"""
1. You’re trying to divide a group into 8 teams. All of you count off and you get the number 
571. Find out your team by computing 571 modulo 8. Save the value to the variable team and 
print out the number. 
"""
team = 571 % 8
print(team)

"""
2. NOTE: The following statements are in order. Please insert variable num where you deem fit.
   HINT: use str(num) method to convert int type to string type for print statement
Please concatenate and print the following statements:
"""
num = 4
part1 = "There was a full moon tonight.\n"
part2 = "Full moons are when the werewolves come out.\n"
part3 = "We saw werewolves "
part4 = " nights ago.\n"
print(part1 + part2 + part3 + str(num) + part4)

# 3. Use the plus equals operator to sum the following sets of numbers:

# a. Sum 94

# b. Sum 1

# c. Sum 98569

# ====== Hamzah's Solution ======
total = 23

total += 94
total += 1
total += 98569

print("The total is: " , total)