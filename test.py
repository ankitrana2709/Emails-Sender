import pandas as pd
cont = pd.read_csv("contacts.csv", header=0)
contacts = cont["recievers"].tolist()
for contact in contacts:
    print(contact)