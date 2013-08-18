# Historical Algorithm Trader v1.10
# --------------------------------
# TBD


# import functions - this needs to import functions from outside
#   had problems with this - Robin to look at.
# keep a record of transactions in array.
# neaten code and more comments
# create an algo that does comparative buy/sell choices...
# user selects how far back to run the algo

# Import sys to run quick checks while debugging
import sys

# Function list
# buy_stock_from_broker
# sell_stock_to_broker
# buy_short_contract_from_broker
# settle_short_contract_with_broker
# read_stocks
# algo


def buy_stock_from_broker(stock_name,stock_value,portfolio,size_of_order):
    global cash
    if cash>size_of_order*stock_value:
        for STOCK in portfolio:
            if STOCK[0]==stock_name:
                if STOCK[2]>0:
                    if size_of_order>STOCK[2]:
                        size_of_order-=STOCK[2]
                        num_of_shares_short=STOCK[2]
                        settle_short_contract_with_broker(stock_name,stock_value,portfolio,num_of_shares_short)
                    else:
                        num_of_shares_short=size_of_order
                        size_of_order=0
                        settle_short_contract_with_broker(stock_name,stock_value,portfolio,num_of_shares_short)
                STOCK[1]+=size_of_order
                cash=cash-(stock_value*size_of_order)-transaction_levy
    else:
        print("Not enough cash to process this buy order!!!")

def sell_stock_to_broker(stock_name,stock_value,portfolio,size_of_order):
    global cash
    for STOCK in portfolio:
        if STOCK[0]==stock_name:
            if size_of_order >=STOCK[1]:
                num_of_shares_short=size_of_order-STOCK[1]
                size_of_order-=num_of_shares_short
                buy_short_contract_from_broker(stock_name,stock_value,portfolio,num_of_shares_short,)
            STOCK[1]-=size_of_order
            cash=cash+(stock_value*size_of_order)-transaction_levy

def buy_short_contract_from_broker(stock_name,stock_value,portfolio,num_of_shares_short):
    global cash
    print("     Have no stock to sell, so buying a short contract!")
    for STOCK in portfolio:
        if STOCK[0]==stock_name:
            STOCK[2]+=num_of_shares_short
            cash=cash+(stock_value*num_of_shares_short)-transaction_levy
            
def settle_short_contract_with_broker(stock_name,stock_value,portfolio,num_of_shares_short):
    global cash
    print("     Settling short contracts with broker before buying more!")
    for STOCK in portfolio:
        if STOCK[0]==stock_name:
            STOCK[2]-=num_of_shares_short
            cash=cash-(stock_value*num_of_shares_short)-transaction_levy

def read_stocks(stock):
    next_entry=""
    end_var=""
    x=1
    y=0
    while x != 99:
        next_char=stock_data.read(1)
        if next_char==",":
            if y==0:
                stock[x][0]=next_entry
                y=1
            else:
                stock[x][1]=float(next_entry)
                y=0
                x+=1
            next_entry=""
        else:        
            next_entry+=next_char
            if next_entry=="x\n":
                next_entry=""
    return(stock)

def algo(All_Stocks,portfolio,percent_diff,tick):
    for STOCK in All_Stocks:
        if STOCK[tick][1]>STOCK[tick-1][1]*percent_diff:
            print("SELL 1 Share in",STOCK[0][0],"for",STOCK[tick][1], " - Date:",STOCK[tick][0])
            sell_stock_to_broker(STOCK[0][0],STOCK[tick][1],portfolio,1)
        elif STOCK[tick][1]<STOCK[tick-1][1]/percent_diff:
            print("BUY 1 Share in",STOCK[0][0],"for",STOCK[tick][1], " - Date:",STOCK[tick][0])
            buy_stock_from_broker(STOCK[0][0],STOCK[tick][1],portfolio,1)

global transaction_levy
transaction_levy=0.5

stock_data=open("AAPL.csv","r")
stock1=[["" for x in range(2)] for y in range(100)]
stock1[0][0]="AAPL"
stock1=read_stocks(stock1)
stock_data.close

stock_data=open("NVDA.csv","r")
stock2=[["" for x in range(2)] for y in range(100)]
stock2[0][0]="NVDA"
stock2=read_stocks(stock2)
stock_data.close


All_Stocks=(stock1,stock2)
# STOCKNAME, num_of_shares, num_of_short_contracts
portfolio=[["AAPL",0,0],["NVDA",0,0]]

# set initial variables
shares=(None,None)
starting_cash=1000
cash=starting_cash
value=1000
total_value=0

# print out the list
print("\nManually created some fake lists of ticks.")
print("(Next step is to draw data from .txt or .csv file)\n")
for STOCK in All_Stocks:
    print("Stock:", STOCK[0][0])
    print(STOCK)
    print("\n\n")



print("Place-holder algorithm will BUY if last tick is x% less than last tick")
print("Will also SELL if last tick is x% more than last tick\n")
percent_diff=-10
while percent_diff<=0 or percent_diff>=100:
    try:
        percent_diff=float(input("Please enter a % between 0 and 100. Decides algorithm logic: "))
    except:
        percent_diff=-10
percent_diff=(percent_diff/100)+1

# fast or slow

answer=""
print("\n")
while answer != "y" and answer !="n":
    print("Would you like to display ALL of the information? y or n?", end=" ")
    answer=input()



# runs through the code printing out each tick and deciding if to trade
print("\nNow running through all the ticks with algorithm:\n")

for tick in range(2, 99):
    if answer=="y":
        print("\n")
        print("Tick [",tick,"]. ",end=" ")
        for STOCK in All_Stocks:
            print(STOCK[0][0], "stock price = ",STOCK[tick][1],"  ",end=" ")

    # run algorithm
    # buys and sells if previous tick is percent_diff% more/less than previous
        print(portfolio)
        print("\nRunning algorithm on stocks....")

    algo(All_Stocks,portfolio,percent_diff,tick)

# Ending Debrief
print("\n\n\nEND OF TRADING!")
print("\nYou have £",cash,"cash.")
print("\nHere is a list of the shares you hold:")
for STOCK in All_Stocks:
    for STOCK2 in portfolio:
        if STOCK2[0]==STOCK[0][0]:
            total_value+=STOCK[tick][1]*STOCK2[1]-STOCK[tick][1]*STOCK2[2]
            print(" ",STOCK2[0],", Shares =",STOCK2[1],"   Short contracts =",STOCK2[2])
total_value+=cash
print("\nYour total value is: £",total_value)
print("\nYour profit/loss is:£",total_value-starting_cash)
print("\nHere is a history of transactions: [need to output to external .txt file")

input ("\nPress The Enter Key To Exit.")

