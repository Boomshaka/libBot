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

import csv

from student import Student
from roomReserve import roomReserve
from gmailLogin import gmailLogin
import RoomID


def sleep():
    time.sleep(random.randint(1,2))


class Dates:
    startDate = datetime.datetime(2019, 10, 25, 0, 0)

    def _init__(self):
        self.idate = datetime.datetime.now()
        self.diffDay = dater - startDate
        self.twelveAM = 0
    
    def setTwelveAM():
        startID = RoomID.StartID
        twelveAM = startID[id] + 816*diffDay.days

class IDList:  
    def _init__(self):
        self.idList = []

    def collectIDList(self):
        startID = RoomID.startID
        dates = Dates()
        dates.setTwelveAM()

        idList.append(dates.twelveAM)
        #print(twelveAM)
        newID = startID[id] + 816*diffDay.days
       
        for x in range(lenGMAIL-1):
            idList.append(newID)
            newID += 4
        idList = list(reversed(idList))



class Main:

    def _init__(self, targetTime, targetRoom):
        self.targetSchedule = targetTime
        self.roomNumber = targetRoom
        self.id = str(self.roomNumber) 

    def main(self):
        #Book rooms 7 days in advance
        
        # print idList
        idList = IDList()
        idList.collectIDList()

        students = []
        with open("credentials.csv") as credentials_csv:
            reader = csv.DictReader(credentials_csv)
            for row in reader:
                students.append(Student(row['username'],row['password']))

        lenGMAIL = len(students)
        thread_list = []
        start = time.time()
        print("Length of gmail, ", lenGMAIL)
        for i in range(lenGMAIL):
            thread = threading.Thread(target = roomReserve, args = (students[i],idList[i],dater,self.targetSchedule,))
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
