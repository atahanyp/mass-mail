import smtplib, ssl
import loop
from email.message import EmailMessage

Email_ADDRESS = "abcde@gmail.com"  #your email adress
Email_PASSWORD = "" # your password


for a in range(len(loop.mailler)):
    with open("mailornek.txt","r+",encoding="utf-8") as f:
        text = f.read().replace("________",loop.sirketler[a],2)
        mail = EmailMessage()
        mail["Subject"] = "Sponsorluk Teklifi"
        mail["From"] = Email_ADDRESS
        mail["To"] = [loop.mailler[a]]
        mesaj = text
        mail.set_content(mesaj)
        print(text)
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(Email_ADDRESS, Email_PASSWORD)
            smtp.send_message(mail)

