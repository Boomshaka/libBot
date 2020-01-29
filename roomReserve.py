

class RoomReserve:

    def roomReserve(student, ID,tdate,targetTime):

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
        browser.find_element_by_id('username').send_keys(student.username)
        browser.find_element_by_id('password').send_keys(student.password)
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