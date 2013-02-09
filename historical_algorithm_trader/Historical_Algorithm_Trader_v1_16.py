# Historical Algorithm Trader v1.13
# --------------------------------
# 

# neaten code and more comments
# create an algo that does comparative buy/sell choices...
# user selects how far back to run the algo
# make the shares inheret from a parent class
# Should save as a .txt file, list of transactions
# Create better variable names (Robin to discuss)
# version all the modules
# add new algo that compares LMA & SMA
# add new algo that keeps a pair-tracking algo

from algo_modules_v1_0 import algo
from modules_v1 import read_stocks

def mainloop(percent_diff,lookback,transaction_levy):

    answer="n"
    shares=(None,None)
    starting_cash=1000000

    total_value=0
    last_value=0

    transaction_history=[""]

    portfolio=[[0,0,0],["AAPL",0,0],["NVDA",0,0]]
    portfolio[0][0] = starting_cash

    stock1=[["" for x in range(2)] for y in range(lookback+1)]
    stock1=read_stocks(stock1,"AAPL",lookback)
    
    stock2=[["" for x in range(2)] for y in range(lookback+1)]
    stock2=read_stocks(stock2,"NVDA",lookback)

    All_Stocks=(stock1,stock2)

    # runs through the code printing out each tick and deciding if to trade
    # print("\nNow running through all the ticks with algorithm:\n")

    for tick in range(2, lookback):
        if answer=="y":
            print("\n")
            #print("Tick [" + tick + "]. ",end=" ")
            for STOCK in All_Stocks:
                pass
                #print(STOCK[0][0] + "stock price = " + STOCK[tick][1] + "  ", end=" ")
            print(portfolio)
            print("\nRunning algorithm on stocks....")

        algo(All_Stocks,portfolio,percent_diff,tick,transaction_history,transaction_levy)

        for STOCK in All_Stocks:
            for STOCK2 in portfolio:
                if STOCK2[0]==STOCK[0][0]:
                    total_value+=STOCK[tick][1]*STOCK2[1]-STOCK[tick][1]*STOCK2[2]
        total_value+=portfolio[0][0]
        if last_value!=total_value:
            text_file2=open("rolling_value.csv","r+")
            whole_thing=text_file2.read()
            lines = [str(total_value) + "," + str(All_Stocks[1][tick][0]) + "\n"]
            text_file2.writelines(lines)
            text_file2.close()
        total_value=0
            
    for STOCK in All_Stocks:
        for STOCK2 in portfolio:
            if STOCK2[0]==STOCK[0][0]:
                total_value+=STOCK[tick][1]*STOCK2[1]-STOCK[tick][1]*STOCK2[2]
                #print(" ",STOCK2[0],", Shares =",STOCK2[1],"   Short contracts =",STOCK2[2])
    total_value+=portfolio[0][0]

    text_file=open("output_file.csv","r+")
    whole_thing=text_file.read()
    lines = [str(percent_diff)+ "," + str(total_value) + "\n"]
    text_file.writelines(lines)
    text_file.close
    #for x in range(len(transaction_history)):
     #   print(transaction_history[x],end=" ")
      #  print(" ")
