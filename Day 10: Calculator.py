def calculate(a,b,c):
    if c=='+':
        return a+b
    if c=='-':
        return a-b
    if c=='*':
        return a*b
    if c=='/':
        return a/b

def calculator():
    n1 = float(input("Choose Your First Number:\n"))
    core = True
    while core:
        op = input("Choose an operator:\n '+' for addition\n '-' for subtraction\n '*' for multiplication\n '/' for division\n ")
        n2 = float(input("Select The Number to be operated on?\n"))
        result = calculate(n1, n2, op)
        print(f"{n1} {op} {n2} = {result}")
        Y = int(input("Press 1 if you would like to continue operation on the result\nPress 2 to clear screen and start a new operation\n"))
        if Y == 1:
            n1 = result
        if Y == 2:
            core = False
            print("\n" * 200)
            calculator()

calculator()
