#import required libraries
# smtplib module is used to send email
import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# class to send email
class Email:
    sender_email = 'example@gmail.com'
    passward = 'example@123'
    port = 587

    def __init__(self,email,product,price,url):
        self.recever_email = email
        self.product = product
        self.price = price
        self.url = url
        self.message = MIMEMultipart('alternative')
        self.message['Subject'] = 'Price fall down...'
        self.message['Form'] = Email.sender_email
        self.message['To'] = email

        self.text = f"""\
        Product: {self.product}\n
        Pirce: {self.price}\n
        check out the link:  {self.url}
        """
        self.html = f"""\
        <html>
            <body>
               <p>
               Product: {self.product}<br>
               Price: {self.price}<br>
               Check out the product 
               <a href="{self.url}">here</a> 
               </p>
            </body>
        </html>
        """
        self.part1 = MIMEText(self.text,'plain')
        self.part2 = MIMEText(self.html,'html')
        self.message.attach(self.part1)
        self.message.attach(self.part2)

    def send_email(self):
        try:
            context = ssl.create_default_context()
            self.server = smtplib.SMTP('smtp.gmail.com',Email.port)
            self.server.ehlo()
            self.server.starttls(context=context)
            self.server.ehlo()
            self.server.login(Email.sender_email,Email.passward)
            self.server.sendmail(
                Email.sender_email,self.recever_email,self.message.as_string()
            )
        except Exception as e:
            print(e)
            return -1
        finally:
            self.server.quit()
