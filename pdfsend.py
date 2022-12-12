from pdf_mail import sendpdf
import config
body = """ Dear Sir, 
            
           Hope you are having a very good day!
           Please find below attachment. Sent by a Script Ankit Rana.
  """
TO= "ankitranastun@gmail.com"
file_name= "ankit"
k = sendpdf(config.EMAIL, TO,
             config.PASSWORD, "Sending pdf in email",
             body, "ankit", "C:/Users/ankit/Documents/GitHub/Python-Mail-Sender")
k.email_send()
print("sent")