import os 
import random

itemsInAuction = ("1995 Chevy Camaro", "Monalisa", "1869 Cardova Wine", "Second World War Veteran Sword", "1000 Years Old Book")
itemToBeAuctioned = random.choice(itemsInAuction)
auctioneersDetails = {}
currentBid = 0
endAuction = False

print("Welcome to SKS Auction house")
print('----------------------------')
print(f"Item to be first put up for the auction: {itemToBeAuctioned}\n")


takePartInAuction = input("Will you like to take part in this auction?\n").lower()
if takePartInAuction == "yes":
    while not endAuction:
        auctioneerName = input('\nWhat is your name?\n')
        bidprice = int(input("\nEnter a bid in dollars \n"))
        auctioneersDetails[auctioneerName] = bidprice
    
        if bidprice > currentBid:
            currentBid = bidprice
    
        userChoice = input("\nWill you like to continue with the auction?\n").lower()
    
        if (userChoice == "no"):
            endAuction = True
        
            for name in auctioneersDetails:
               if auctioneersDetails[name] == currentBid:
                   print(f"\nCongratulations {name} you won the auction for the {itemToBeAuctioned} with a bid of ${currentBid}.\n\n\n")
                   break
               else: 
                   continue
        
        elif userChoice == "yes":
            os.system("cls")
            
    #print(auctioneersDetails)
    
elif takePartInAuction == "no":
    print("\nAlright then hope you take part in the next.\n")
    print("Goodbye for now.\n\n")
    

