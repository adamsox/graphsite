# isAPIDown.py

from course_searcher import search_course
import smtplib
import time

# email info
gmail_user = 'cis3760team10dev@gmail.com'
gmail_password = 'ThisIsAPassword@123'

sent_from = gmail_user
to = ['cis3760team10dev@gmail.com']

subject = 'API Error Alert'
body = 'Urgent error, API is potentially down! An error occured when trying to call from the API'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

def send_email():
    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to, email_text)
        smtp_server.close()
        print ("Error email sent successfully!")
    except Exception as ex:
        print ("Something went wrong while emailing.",ex)

def check_api():
    try:
        api_input = ['cis', 'x', 'x']
        
        ret_val = search_course(api_input)
        
        check_list = isinstance(ret_val, list)
        
        if check_list:
            print("Success!")
        else:
            print("Return Value Error.")
            send_email()
        
    except:
        print("API Error.")
        
        send_email()
            
def main():
    while True:
        check_api()
        
        # wait 30 minutes
        time.sleep(1800)
        
main()
