from modules_v1 import buy_stock_from_broker
from modules_v1 import sell_stock_to_broker
from modules_v1 import buy_short_contract_from_broker
from modules_v1 import settle_short_contract_with_broker

def algo(All_Stocks,portfolio,percent_diff,tick,transaction_history,transaction_levy):
    for STOCK in All_Stocks:
        if STOCK[tick][1]<STOCK[tick-1][1]/percent_diff:
            sell_msg=["SELL 1 Share in",STOCK[0][0],"for",STOCK[tick][1], " - Date:",STOCK[tick][0]]
            transaction_history+=[sell_msg]
            #print("SELL 1 Share in",STOCK[0][0],"for",STOCK[tick][1], " - Date:",STOCK[tick][0])
            sell_stock_to_broker(STOCK[0][0],STOCK[tick][1],portfolio,1000,transaction_levy)
        elif STOCK[tick][1]>STOCK[tick-1][1]*percent_diff:
            buy_msg=["BUY 1 Share in",STOCK[0][0],"for",STOCK[tick][1], " - Date:",STOCK[tick][0]]
            transaction_history+=[buy_msg]
            #print("BUY 1 Share in",STOCK[0][0],"for",STOCK[tick][1], " - Date:",STOCK[tick][0])
            buy_stock_from_broker(STOCK[0][0],STOCK[tick][1],portfolio,1000,transaction_levy)
