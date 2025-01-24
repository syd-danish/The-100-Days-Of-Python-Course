auction_bid={}

def auction():
    array = []
    name=input("What is the name of the bidder?\n")
    amt=int(input("How much Amount would they bid?\n"+"$"))
    array.append(amt)
    auction_bid[name]=amt
    more_bid=int(input("Are there any others who would like to bid?\n Press 1 for Yes\n Press 2 for No\n"))
    if more_bid==1:
        print("\n"*100)
        auction()
    if more_bid==2:
        winning_bid=max(array)
        for key,value in auction_bid.items():
            if value==winning_bid:
                print("The Winner is of the auction is: \n"+ str(key))
        exit()




print("Welcome to the Auction!")
auction()
