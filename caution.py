logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Bid-program".center(50," "))
bid_dict={}
should_continue=False
def highest_bid(bid_records):
    highest_bid=0
    winner=""
    for bidder in bid_records:
        score=bid_records[bidder]
        if score>highest_bid:
            highest_bid=score
            winner=bidder
    print(f"highest bid is {highest_bid} by {winner}")
while  not should_continue:
    name = input("enter the name: ")
    amount=int(input("enter the amount to bid: "))
    bid_dict[name]=amount
    n=input("enter the yes or no: ").lower()
    if n=="yes":
        should_continue=False
    else:
        highest_bid(bid_dict)
        should_continue=True

    

        




