import smtplib

def send_followup(email):
    msg = "Thank you for using CareerBoost. Your applications are being processed."
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("noreply@careerboost.com", "hidden-password")
    server.sendmail("noreply@careerboost.com", email, msg)
    return True
