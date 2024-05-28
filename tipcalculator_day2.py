print("Welcome to tip calculator")
total = int(input("Enter the total amount $ "))
tip = int(input("Enter the tip percentage 10 ,12,15 ?"))
split = int(input("Enter the number would like to split the amount "))
tip_p= total/tip *100
total_amount = total + tip_p
share_amount = round(total_amount/split)
print(f"Each person should pay {share_amount}")




