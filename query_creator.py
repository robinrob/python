import csv

query = "SELECT Id, Alumina__Google_Attendees__c, Alumina__Google_Id__c, Alumina__Salesforce_Id__c FROM Alumina__Google_Event_Attendees__c WHERE Alumina__Google_Id__c IN ("

with open('jpress_google_ids.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if reader.line_num == 1:
            continue
            
        query += "\'" + str(row[0]) + "\', "
        
    query = query[0:len(query) - 2]
        
query += ")"

print str(query)