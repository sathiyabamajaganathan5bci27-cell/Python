import smtplib

def send_email():
    server = smtplib.SMTP('://gmail.com', 587)
    server.starttls()
    server.login('your_email@gmail.com', 'your_app_password')
    server.sendmail('from@gmail.com', 'to@gmail.com', 'Subject: Happy Birthday!\nHave a great day!')
    server.quit()
