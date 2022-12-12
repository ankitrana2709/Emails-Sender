import smtplib
from email.mime.text import MIMEText  #use from email.message import Message so that you can set content,add attachement. 
import config
if __name__=="__main__":
  server=smtplib.SMTP('smtp.gmail.com',587)

  server.starttls()

  EMAIL=config.EMAIL
  PASSWORD=config.PASSWORD
  server.login(EMAIL,PASSWORD)

  message=MIMEText("Sent from py")
  message["From"]=EMAIL
  TO="ankitranastun@gmail.com"
  message["To"]= TO
  message["Subject"]="Hello World"

  server.sendmail(EMAIL,TO,message.as_string())

  print("Mail is successfully sent")
