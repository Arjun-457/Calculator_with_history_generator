print("--WELCOME TO ARJUN CALCULATOR--")
print("What type of operation you want to do")

operation = (input("Enter\n a for Add\n s for Subtract\n m for Multiply\n d for Division:").strip().lower())

if operation == "a":
    print("Oh you want to do Addition")
    n = int(input("Enter how many number you want to add: "))
    total = 0.0
    history=[]
    for i in range(n):
        num = float(input(f"Enter the {i+1} Number:  "))
        total+=num
        history.append(str(num))
    
    print(f"The sum is {total}")
    history_str = " + ".join(history)
    with open ("history.txt", "a") as f:
        f.write(f"{history_str} = {total}" + "\n")
        
elif operation == "s":
    print("Oh you want to do Subtraction")
    f = float(input("Enter the greater number:  "))
    s = float(input("Great! Now the smaller one:  "))
    result = (f-s)
    print(f"The difference is {result}")
    
    with open("history.txt","a") as j:
        j.write(f"{f} - {s} = {result}" + "\n")
        
elif operation == "m":
    print("Oh you want to do Multiplication")
    n = int(input("Enter how many number you want to multiply: "))
    product = 1.0
    history=[]
    for i in range(n):
        num = float(input(f"Enter the {i+1} Number:  "))
        product*=num
        history.append(str(num))
        
    print(f"The product is {product}")
    history_str = " X ".join(history)
    
    with open ("history.txt", "a") as f:
        f.write(f"{history_str} = {product}" + "\n")  
            
elif operation == "d":
    print("Oh you want to do Division")
    n = float(input("Enter the divident:  "))
    d = float(input("Great! Now enter divisor:  "))
    result = (n/d)
    print(f"The quotient is {result}")
    
    with open("history.txt","a") as j:
        j.write(f"{n} / {d} = {result}" + "\n")
        
else:
    print("Invalid operation. Exiting...")
