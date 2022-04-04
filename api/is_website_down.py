# isWebsiteDown.py

import asyncio
from playwright.async_api import async_playwright
import smtplib
import time

# website info
web_url = 'http://131.104.49.112/'

# email info
gmail_user = 'cis3760team10dev@gmail.com'
gmail_password = 'ThisIsAPassword@123'

sent_from = gmail_user
to = ['cis3760team10dev@gmail.com']

subject = 'Website Error Alert'
body = 'Urgent error, website is potentially down! Automated testing was unable to connect to the website'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

async def run(playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = await chromium.launch()
    page = await browser.new_page()
    
    try:
        # try to connect to the web
        await page.goto('http://131.104.49.112/')
    
        print("Successful connection!")
        
        title = await page.title()
        print("Title: " + title)
    except:
        # send error email if website is down
        print("Error, could not connect to website.")
        
        try:
            smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            smtp_server.ehlo()
            smtp_server.login(gmail_user, gmail_password)
            smtp_server.sendmail(sent_from, to, email_text)
            smtp_server.close()
            print ("Error email sent successfully!")
        except Exception as ex:
            print ("Something went wrong while emailing.",ex)
    
    #time.sleep(5)
    
    
    await browser.close()

async def main():
    while True:
        async with async_playwright() as playwright:
            await run(playwright)
            
        # wait 30 minutes
        time.sleep(1800)
        
asyncio.run(main())
