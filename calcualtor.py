logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)
def add(num1 ,num2):
    return num1 + num2 
def sub(num1 , num2):
    return num1 - num2
def mul(num1 , num2):
    return num1 * num2
def div(num1 ,num2):
    return num1 / num2
def modl(num1 , num2):
    return num1 % num2
stop = False
while not stop:
    operators={"+":add,"-":sub ,"*":mul,"/":div,"%":modl}
    num1 = int(input("enter the first number: "))
    num2 = int(input("enter the second number: "))
    for symbol in operators:
        print(symbol)
    sy = input("enter the operation symbol: ")
    v=operators[sy]
    result = v(num1,num2)
    print(f"{num1} {sy} {num2} = {result}")
    n=input("enter 'y' for continue with last ans as one ele or enter 'n' for new cal: ").lower()
    if n =="y":
        num3 = int(input("enter the new numer: "))
        sy = input("enter the operation symbol: ")
        v=operators[sy]
        result1= v(result,num3)
        print(f"{result} {sy} {num3} = {result1}")
    if n=="n":
        v(num1,num2)
        


