import imaplib
import re


# function to read last email message
def get_otp_from_email(email_credentials=None):
    mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    mail.login(email_credentials['email'], email_credentials['password'])
    mail.select("INBOX")
    result, data = mail.search(None, "ALL")
    ids = data[0]
    id_list = ids.split()
    latest_email_id = id_list[-1]
    result, data = mail.fetch(latest_email_id, "(RFC822)")
    raw_email = data[0][1]
    re_match = re.search(r'Your OTP is (\d{6})', str(raw_email))
    otp = re_match.groups()[0]
    return otp
