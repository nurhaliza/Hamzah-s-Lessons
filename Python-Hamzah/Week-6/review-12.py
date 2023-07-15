"""
1. Write a program that determines whether an input is one of the following Korean dishes: 
Buldak Noodles, Ttebokki, Soondubu, or Japchae. 
Please use if, else if, and else statements for your conditions. 
"""

# Hamzah's Solution
"""
if korean_food == "Soondubu":
     print("Soondubu is great with kimchi and the touch of the soft tofu just melts in your mouth!")
else korean_food == "Ttebboki":
     print("I also love Ttebokki because of their spicy sauce and their rice cake, they have a lot of flavor!")
else if korean_food == "Buldak Noodles":
     print("Out of the Korean foods that I like, I love the Buldak Noodles a lot because of their sauce, its really spicy.")
"""

food = "spoondubu"
# Ngah's Solution
if food == "Soondubu" or food == "soondubu":
    print("Soondubu")
elif food == "Tteobokki" or food == "tteobokki":
    print("Tteobokki")
elif food == "Buldak Noodles" or food == "buldak noodles":
    print("Buldak Noodles")
elif food == "Japchae" or food == "japchae":
    print("Japchae")
else:
    print("Not Korean Food.")


"""
2. Write a program that determines whether a grade is pass or fail. 
A passing grade is either an A, B or C. A failing grade is anything else 
besides the passing grades. Please use if, else if, and else statements for your conditions. 
"""
"""
# Hamzah's Solution
my_subject_history = "A+"
print((my_subject_history))

my_subject_math = "B"
print((my_subject_math))

my_subject_english = "D+"
print((my_subject_english))

my_subject_science = "A-"
print((my_subject_science))
"""

# Ngah's Solution
grade = "r"
if grade == "A" or grade == "a" or grade == "B" or grade == "b" or grade == "C" or grade == "c":
    print("It is a passing grade.")
elif grade == "F" or grade == "f":
    print("It is a failing grade.")
else: 
    print("It is an invalid grade.")