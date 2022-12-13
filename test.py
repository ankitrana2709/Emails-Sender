import pandas as pd
contacts = ['indiands.csv', 'contacts.csv']
for contact in contacts:
    cont = pd.read_csv(contact, header=0)
    con = cont["recievers"].tolist()
print(con)
    
