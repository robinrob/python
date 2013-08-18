def buy_stock_from_broker(stock_name,stock_value,portfolio,size_of_order,transaction_levy):
    cash = portfolio[0][0]
    for STOCK in portfolio:
        if STOCK[0]==stock_name and cash>=size_of_order*stock_value:
            if STOCK[2]>0 and size_of_order>STOCK[2]:
                size_of_order-=STOCK[2]
                num_of_shares_short=STOCK[2]
                settle_short_contract_with_broker(stock_name,stock_value,portfolio,num_of_shares_short,transaction_levy)
            elif STOCK[2]>0 and size_of_order<=STOCK[2]:
                num_of_shares_short=size_of_order
                size_of_order=0
                settle_short_contract_with_broker(stock_name,stock_value,portfolio,num_of_shares_short,transaction_levy)
            STOCK[1]+=size_of_order
            cash=cash-(stock_value*size_of_order)-transaction_levy
        elif STOCK[0]==stock_name and cash<(size_of_order*stock_value-transaction_levy):
            nothing=""
            #print("NOT ENOUGH MONEY TO BUY!!!")
    portfolio[0][0]=cash

def sell_stock_to_broker(stock_name,stock_value,portfolio,size_of_order,transaction_levy):
    cash = portfolio[0][0]
    for STOCK in portfolio:
        if STOCK[0]==stock_name:
            if size_of_order >STOCK[1]:
                num_of_shares_short=size_of_order-STOCK[1]
                size_of_order-=num_of_shares_short
                buy_short_contract_from_broker(stock_name,stock_value,portfolio,num_of_shares_short,transaction_levy)
            STOCK[1]-=size_of_order
            cash=cash+(stock_value*size_of_order)-transaction_levy
    portfolio[0][0]=cash

def buy_short_contract_from_broker(stock_name,stock_value,portfolio,num_of_shares_short,transaction_levy):
    cash = portfolio[0][0]
#    print("     Have no stock to sell, so buying a short contract!")
    for STOCK in portfolio:
        if STOCK[0]==stock_name:
            STOCK[2]+=num_of_shares_short
            cash=cash+(stock_value*num_of_shares_short)-transaction_levy
    portfolio[0][0]=cash
            
def settle_short_contract_with_broker(stock_name,stock_value,portfolio,num_of_shares_short,transaction_levy):
    cash = portfolio[0][0]
    #print("     Settling short contracts with broker before buying more!")
    for STOCK in portfolio:
        if STOCK[0]==stock_name:
            STOCK[2]-=num_of_shares_short
            cash=cash-(stock_value*num_of_shares_short)-transaction_levy
    portfolio[0][0]=cash

def read_stocks(stock,stock_name,lookback):
    next_entry=""
    end_var=""
    x=1
    y=0
    stock[0][0]=stock_name
    stock_name=stock_name + ".csv"
    stock_data=open(stock_name,"r")
    while x < lookback+1:
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
        if next_char=="&":
            x=lookback+1
    stock_data.close
    return(stock)
