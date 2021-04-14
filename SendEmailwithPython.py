import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path #similar to os.path

html = Template(Path('index.html').read_text())
email = EmailMessage()
# Enter your name i.e. senders name
email['from'] = 'Senders name'                    
# Enter receiver's email id
email['to'] = 'recievers@emailid.com'             
# Your message
email['subject'] = 'You won 1,000,000 $ dollars!' 

email.set_content(html.substitute({'name':'TinTin'}),'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    # Enter your email login details
    smtp.login('your@email.com', 'YourEmailPassword')   
    smtp.send_message(email)
    print('all good boss!')
