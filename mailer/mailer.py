from smtplib import SMTP as smtp
from email.mime.text import MIMEText as text
#Config File can be found in the repository. Please have the file in the same location as the mailer code.
import MailerConfig as config

class SendMail(object):
   template_name = ''
   def __init__(self):
      self.server = smtp(config.MAIL_SERVER_NAME+":"+str(config.MAIL_SERVER_PORT))
      if config.MAIL_SERVER_USE_TLS:
         self.server.starttls()
      self.server.login(config.FROM_ID,config.FROM_PASSWORD)

   def make_mail(self):
      subject,mail_body=("You've received a mail","Hi, you have successfully triggered the mail! Congrats :D")
      msg = text(mail_body)
      msg['Subject'] = subject
      return msg

   def send_mail(self,to_address):
      msg = self.make_mail()
      try:
         self.server.sendmail(config.FROM_ID, to_address, msg.as_string())
         print 'sent'
      except:
         print 'error'
   def __del__(self):
      self.server.quit()

to_address = raw_input('Enter the address to which the mail needs to be sent: ')
s = SendMail()
s.send_mail(to_address)
