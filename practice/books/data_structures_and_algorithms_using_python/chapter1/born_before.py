from datetime import date
from dateutil.relativedelta import relativedelta

def main():
    BORN_BEFORE = date.today() + relativedelta(years=-21)
    user_date = promptAndExtractDate()
    
    while user_date is not None:
        if user_date <= BORN_BEFORE:
            print("Is at least 21 years of age: ", user_date)
        else:
            print("Yo fackin' young!")
            
        user_date = promptAndExtractDate()


def promptAndExtractDate():
    print ("Enter a birth date.")
    month = int(input("month (0 to quit): "))
    if month == 0:
        return None
    else :
        day = int(input("Day: "))
        year = int(input("Year: "))

    return date(year, month, day)

main()

