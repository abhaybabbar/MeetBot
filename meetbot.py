from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import datetime
import time
import os
import keyboard




class meet_bot:
    def __init__(self):
        
        # To give permission to chrome pop-up
        opt = Options()
        opt.add_argument("--disable-infobars")
        opt.add_argument("start-maximized")
        opt.add_argument("--disable-extensions")
        # Pass the argument 1 to allow and 2 to block
        opt.add_experimental_option("prefs", { \
        "profile.default_content_setting_values.media_stream_mic": 1, 
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 2, 
        "profile.default_content_setting_values.notifications": 2 
        })
        self.bot = webdriver.Chrome(chrome_options=opt,executable_path = "C:\Program Files (x86)\chromedriver.exe")
        
        
    
    def login(self, email, passw, link):
        

        
        bot = self.bot
        # This is for the google meet sign in page
        bot.get("https://accounts.google.com/signin/v2/identifier?ltmpl=meet&continue=https%3A%2F%2Fmeet.google.com%3Fhs%3D193&&o_ref=https%3A%2F%2Fmeet.google.com%2F_meet%2Fwhoops%3Fsc%3D232%26alias%3Dmymeetingraheel&_ga=2.262670348.1240836039.1604695943-1869502693.1604695943&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
        time.sleep(2)
        
        
        # This is for the Email address block
        email_in = bot.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
        email_in.send_keys(email)
        
        
        # To click the 'next' button
        next_btn = bot.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]")
        next_btn.click()
        time.sleep(5)
        
        # Password block
        passwo = bot.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
        passwo.send_keys(passw)
        
        # To click the 'next' button
        bot.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]').click()
        time.sleep(5)
        
        # To input the google meet link
        link_var = bot.find_element_by_xpath('/html/body/c-wiz/div/div[2]/div/div[1]/div[3]/div[2]/div[1]/label/input')
        link_var.send_keys(link)
        
        # To click 'Join' button
        bot.find_element_by_xpath('/html/body/c-wiz/div/div[2]/div/div[1]/div[3]/div[2]/div[2]/button/div[2]').click()
        time.sleep(10)
        
        # To click 'Join Now' button
        bot.find_element_by_xpath('/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span').click()
        time.sleep(10)
        
        # To click on the participants section
        bot.find_element_by_xpath('/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[1]/div[3]/div/div[2]/div[1]/span').click()
        time.sleep(2)
        
        # To get the name of all the participants
        namelist = bot.find_elements_by_class_name("ZjFb7c")
        i = 1
        for name in namelist:
            print("Person - ", i, name.get_attribute('innerHTML'))
            i+=1

        
        
        
obj = meet_bot()
obj.login("Enter Mail","Enter Password", 'Enter meeting link')


