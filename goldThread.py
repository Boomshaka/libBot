import threading
from multiprocessing import Queue
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import datetime
from datetime import date
import imaplib
from email.message import EmailMessage
from email.parser import BytesParser, Parser
import random
from html.parser import HTMLParser

global dater
global linkList

startID = {
    "2314": 647760737,
    #"2334": 647761073,
    "2334": 681587672,
    "2308": 647760593,
    "2310": 647760641,
    "2312": 647760684,
    "2316": 647760785,
    "2318": 647760833,
    #"2326": 647760881,
    "2326": 681587480,
    #"2328": 647760929,
    "2328": 681587528,
    #"2330": 647760977
    "2330": 681587576,
    #"2332": 647761025,
    "2332": 681587624,
    #"2336": 647761121
    "2336": 681587720,
    "2338": 647761169,
    "2501": 647761217,
    "2528": 647761313,
    "2574": 648692976,
}


lenGMAIL = len(username)
#61109393Ap$$ for andy ucsb.edu email
#Missamerica2! for colin ucsb.edu email
#Thelong1 for francispyon ucsb.edu email


def sleep():
    time.sleep(random.randint(1,2))

def gmailLogin(username, password):

    time.sleep(10) #new
    #Log into ucsb gmail and find latest email ID
    print(username)
    username = username + '@ucsb.edu'
    M = imaplib.IMAP4_SSL('imap.gmail.com')
    M.login(username, password)
    M.select('inbox')
    rv, data = M.search(None, 'ALL')
    mail_ids = data[0]
    id_list = mail_ids.split()
    latest_email_id =id_list[-1]

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

def roomReserve(username, password, ID,tdate,targetTime):

    #Open libcal website and go to correct month
    #browser = webdriver.Chrome('/Users/benliu/Documents/LIBBOT/chromedriver')
    browser = webdriver.Chrome('/Users/shakakanenobu/libBot/chromedriver')
    browser.get('https://libcal.library.ucsb.edu/rooms.php?i=12405')
    select = Select(browser.find_element_by_class_name('ui-datepicker-month'))
    select.select_by_value(str(tdate.month - 1))
    time.sleep(.25)
    browser.find_element_by_link_text(date.strftime(tdate,"%d").lstrip('0')).click()
    time.sleep(4)
    ID = targetTime*2 + ID
    #print("ID for ", username, " is ", ID)

    sleep(5)
    #click 4 time slots, total 2 hours
    for x in range(4):
        ID = int(ID)
        ID = str(ID)
        browser.find_element_by_id(ID).click()
        ID = int(ID)
        ID += 1
        time.sleep(.25)

    #get to the next screen
    browser.find_element_by_name('Continue').click()
    browser.find_element_by_id('s-lc-rm-sub').click()

    #loginUCSB
    browser.find_element_by_id('username').send_keys(username)
    browser.find_element_by_id('password').send_keys(password)
    sleep()
    browser.find_element_by_name('submit').click()

    sleep()

    #send Group Name
    browser.find_element_by_id("nick").send_keys('Nintendo Co. Customer Support')
    browser.find_element_by_name('Submit').click()
    print (datetime.datetime.now())
    sleep()
    browser.close()
    browser.quit()

def main(targetTime, targetRoom):
    startDate = datetime.datetime(2019, 10, 25, 0, 0)
    idate = datetime.datetime.now()#datetime.datetime(2019, 1, 28,0,0)
    timeSchedule = targetTime
    roomNumber = targetRoom
    id = str(roomNumber)

    tdate = datetime.datetime(idate.year, idate.month, idate.day, timeSchedule, 0)

    #Book rooms 7 days in advance
    dater = tdate + datetime.timedelta(days = 14)


    diffDay = dater - startDate
    twelveAM = startID[id] + 816*diffDay.days
    idList = []
    idList.append(twelveAM)
    #print(twelveAM)
    newID = startID[id] + 816*diffDay.days
    #+ 2*(diffDay.seconds/3600)
    #print(diffDay.seconds/3600)
    #print(newID)
    for x in range(lenGMAIL-1):
        idList.append(newID)
        newID += 4
    idList = list(reversed(idList))
    # print idList

    thread_list = []
    start = time.time()
    print("Length of gmail, ", lenGMAIL)
    for i in range (lenGMAIL):
        thread = threading.Thread(target = roomReserve, args = (username[i],password[i],idList[i],dater,targetTime,))
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join()

    print ('total time taken:' , time.time()-start)

    for k in range(lenGMAIL):
        linkList = []

        try:
            gmailLogin(username[k], password[k])
            print ('Successful confirmation for:', username[k])
        except Exception:
            print ('an error has occured with the following username, trying next username', username[k])
            pass
if __name__ == "__main__":
    while True:
        #wait for midnight
        while datetime.datetime.now().hour == 0:
            print ('sleeping ... ' , datetime.datetime.now())
            time.sleep(1)
            #start booking at 12pm
        main(12, 2336)
        print ('sleeping for one hour...')
        time.sleep(3600)
        # print 'sleeping for one hour...'
        # time.sleep(3600)
