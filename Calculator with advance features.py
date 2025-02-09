import math #Math functions use karne ke liye
# Calculation history store karne ke liye
history = []

while True:
    print("\nPro Calculator (Type 'exit' to stop)")
    num1 = input("Pehla number likho: ")

    # Agar user 'exit' likhe, toh program band ho
    if num1.lower() == "exit":
        print("\nCalculation History:")
        for h in history:
            print(h)
        print("\nCalculator Band Ho Gaya! ")
        break

    
    num1 = float(num1)
    operator = input("Operator choose karo (+, -, *, /, ^, sqrt, !, %, log, sin, cos, tan, sqr, cube, lcm, gcd, temp, currency): ")

    # Square Root ke liye direct calculation
    if operator == "sqrt":
        result = math.sqrt(num1)

    # Square & Cube Calclation
    elif operator == "sqr":
        result = num1 ** 2
    elif operator == "cube":
        result = num1 ** 3

    
    # Factorial Calculation
    elif operator == "!":
        if num1 >= 0 and num1.is_integer():
            result = math.factorial(int(num1))
        else:
            result = "Error! Factorial sirf positive integers ke liye hota hai."

    # Modulus (Remainder) Calculation
    elif operator == "%":
        num2 = float(input("Doosra number likho: "))
        result = num1 % num2

    # Logarithm Calculation
    elif operator == "log":
        if num1 > 0:
            result = math.log(num1)
        else:
            result = "Error! Logarithm sirf positive numbers ke liye hota hai."

    # Trignometric Functions
    elif operator == "sin":
        result = math.sin(math.radians(num1))
    elif operator == "cos":
        result = math.cos(math.radians(num1))
    elif operator == "tan":
        result = math.tan(math.radians(num1))

    # Power (Exponentiation)
    elif operator == "^":
        num2 = float(input("Doosra number likho: "))
        result = num1 ** num2

    # LCM & GCD Calculation
    elif operator == "lcm":
        num2 = int(input("Doosra number likho: "))
        result = math.lcm(int(num1), num2)
    elif operator == "gcd":
        num2 = int(input("Doosra number likho: "))
        result = math.gcd(int(num1), num2)

    # Temprature Conversion
    elif operator == "temp":
        unit = input("Celsius to Fahrenheit (C) ya Fahrenheit to Celsius (F) choose karo: ").lower()
        if unit == "c":
            result = (num1 * 9/5) + 32 # Celsius to Fahrenheit
        elif unit == "f":
            result = (num1 - 32) * 5/9 # Fahrenheit to Celsius
        else:
            result = "Invalid temperature unit!"

    # Currency Conversion (Static Conversion Rate)
    elif operator == "currency":
        currency_type = input("INR to USD (I) ya USD to INR (U) choose karo: ").lower()
        if currency_type == "i":
            result = num1 / 83 # 1 USD = 83 INR (Static Rate)
        elif currency_type == "u":
            result = num1 * 83
        else:
            result = "Invalid currency type!"
            
        
    # Basic Operations
    else:
        num2 = float(input("Doosra number likho: "))
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error! Zero se divide nahi kar sakte."
        else:
            result = "Invalid operator!"

    # History me store karna
    history.append(f"{num1} {operator} {num2 if 'num2' in locals() else ''} = {result}")

    # Output print karna
    print("Result:", result)
    
        

