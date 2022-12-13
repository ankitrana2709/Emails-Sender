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
body = """ Dear Sir, <br> <br> Hope you are having a very good day!
   <br><br> This is Ankit Rana <br>Hello sir, 
I am a fellow data scientist looking for an opportunity to learn and grow. If there is an opportunity in your firm pls let me know.<br>
Kindly reach out for your valuable feedbacks.<br><br>
Thankyou.<br><a href="https://swamizone.vercel.app/"> Ankit Rana</a><br> https://swamizone.vercel.app/
 
  """
contacts = ["ankitranastun@gmail.com","ankit@scatterpie.io"]
counter = 0
contacts= ['contacts.csv', 'indiands.csv']
for cont in contacts:

    conts = pd.read_csv(cont, header=0)
    contacts = conts["recievers"].tolist()
    for contact in contacts:
        message = MIMEMultipart()
        message['From'] = email_id
        message['To'] = contact
        message['Subject'] = "Seeking to learn"

        message.attach(MIMEText(body, 'html'))

        #attach pdf here
        pdfs = ['AnkitRana.pdf', 'CoverLetter.pdf', 'thanks.pdf']
        for pdf in pdfs:
            binary_pdf = open(pdf, 'rb')

            payload = MIMEBase('application', 'octate-stream', Name=pdf)
            payload.set_payload((binary_pdf).read())
            
            # enconding the binary into base64
            encoders.encode_base64(payload)
            
            # add header with pdf name
            payload.add_header('Content-Decomposition', 'attachment', filename=pdf)
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