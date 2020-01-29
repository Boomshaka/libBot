import student.py
import time
import imaplib
from email.parser import BytesParser, Parser
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import datetime
from datetime import date


class GmailLogin:
    #Input: instance of Student class
    # class Student:
    #     def _init__(self, username, password):
    #         self.username = username + '@ucsb.edu'
    #         self.password = password
    #         self.lenGMAIL = len(self.username)

    M = imaplib.IMAP4_SSL('imap.gmail.com')

    def gmailLogin(student):
        time.sleep(10) #new
        #Log into ucsb gmail and find latest email ID
        print(student.username)
        M.login(student.username, student.password)
        
        

        #Access latest email
        sleep()
        typ, msg_data = M.fetch(latest_email_id, '(RFC822)')
        msg = Parser().parsestr(str(msg_data[0][1]))
        msg=str(msg)

        #Set msg equal to the confirmation link
        index1 = msg.index('https://libcal.library.ucsb.edu/confirm')
        msg = msg[index1:index1+138]
        print(msg)
        M.close()
        M.logout()

        #Open up confirmation link and confirm rooms
        #browser = webdriver.Chrome('/Users/benliu/Documents/LIBBOT/chromedriver')
        browser = webdriver.Chrome('/Users/shakakanenobu/libBot/chromedriver')
        browser.get(msg)
        sleep()
        browser.find_element_by_id('rm_confirm_link').click()
        browser.close()


class SelectMail:

    def newestID():
        mailBox = GmailLogin()
        mailBox.M.select('inbox')
        rv, data = mailBoxM.search(None, 'ALL')
        mail_ids = data[0]
        id_list = mail_ids.split()
        latest_email_id =id_list[-1]