from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import os
from email import encoders
import pandas as pd
from email.mime.multipart import MIMEMultipart
import smtplib
import config
email_id=config.EMAIL
email_passwd=config.PASSWORD
#email_id = os.environ.get("EMAIL_USER")
#email_passwd = os.environ.get("EMAIL_PASS")
body = """ Dear Ma'am, <br> <br> Hope you are having a very good day!
   <br> Please find below attachment. <br><br> Ankit Rana <br>This mail is sent by a script created by a <br>
   <a href="swamizone.vercel.app">Mathematician</a>.
  """
#contacts = ["ankitranastun@gmail.com","ankit@scatterpie.io"]
counter = 0
cont = pd.read_csv("contacts.csv", header=0)
contacts = cont["recievers"].tolist()
for contact in contacts:
    message = MIMEMultipart()
    message['From'] = email_id
    message['To'] = contact
    message['Subject'] = "Please find my looped attachment below"

    message.attach(MIMEText(body, 'html'))

    #attach pdf here
    pdfname = 'lvu.pdf'
    binary_pdf = open(pdfname, 'rb')

    payload = MIMEBase('application', 'octate-stream', Name=pdfname)
    payload.set_payload((binary_pdf).read())
    
    # enconding the binary into base64
    encoders.encode_base64(payload)
    
    # add header with pdf name
    payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
    message.attach(payload)

    session = smtplib.SMTP('smtp.gmail.com', 587)
    
    #enable security
    session.starttls()
    
    #login with mail_id and password
    session.login(email_id, email_passwd)
    
    text = message.as_string()
    session.sendmail(email_id, contact, text)
    session.quit()
    print(f'Mail Sent to {contact}')
    counter +=1
if counter == 1:
    print("One mail sent")
else:
    print(f"Total {counter} mails sent.")