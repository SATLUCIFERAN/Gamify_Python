
# utils.py

def get_int(prompt):       
       
    while True:
        s = input(prompt)          # 1. Show the prompt (prompt)
                                   #    & Loop until the user types only digits 
        if s.isdigit():            # 2. Validate it’s digits
            return int(s)          # 3. Convert & return
        print("Please enter a whole number.\n")


