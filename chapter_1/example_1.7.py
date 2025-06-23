
age_str = input("Enter your age: ")    # age_str is still text
if age_str.isdigit():                   # validate that it’s all digits
    age = int(age_str)                  # convert to integer
    print(f"You are {age} years old.")
else:
    print("Please enter a valid whole number for age.")

'''
Enter your age: 20
You are 20 years old.
'''


