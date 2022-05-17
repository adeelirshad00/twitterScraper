#!/usr/bin/env python
# coding: utf-8

# In[52]:


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

from time import sleep

chrome_options = Options()
driver=webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
driver.maximize_window()

chrome_options = Options()
# driver=webdriver.Edge(executable_path=r'./driver/msedgedriver.exe')

driver.maximize_window()
website='https://twitter.com/i/flow/login'
driver.get(website)
print('website loading')
sleep(5)
username = driver.find_element_by_xpath('//input[@name="text"]')

username.send_keys('')
print('username done')
username.send_keys(Keys.RETURN)
sleep(2)

password = driver.find_element_by_xpath('//input[@name="password"]')
print('password done')
sleep(2)

password.send_keys('')
password.send_keys(Keys.RETURN)



# In[53]:


website='https://twitter.com/adl440/followers'
driver.get(website)
print('website loaded')


# In[54]:


def get_tweet_data(card):
    try:
        username = card.text
    except Exception:
        return
    return username


# In[ ]:


import csv
import time
import pandas as pd
from time import sleep
import csv
import random

    
data = []
counter = 0
last_position = driver.execute_script("return window.pageYOffset;")
scrolling = True
tweet_data = []
tweet_ids = set()
count = 1
starting_time = time.time()

with open(f"test{random.randint(0,1999)}.csv", "wt", newline="",encoding='utf-8') as fp:
    writer = csv.writer(fp, delimiter=",")
    while scrolling:
        sleep(2)
        page_cards = driver.find_elements_by_xpath('.//div[@data-testid="primaryColumn"]//section//span[contains(text(), "@")]')
        print('cards length:',len(page_cards))
        for card in page_cards[-20:]:
            count = count + 1
            tweet = get_tweet_data(card)
            if tweet:
                tweet_id = ''.join(tweet)
                if tweet_id not in tweet_ids:
                    tweet_ids.add(tweet_id)
                    data.append(tweet)
                    writer.writerow([tweet])
                    print(count, 'username: ', tweet)
    #              

        scroll_attempt = 0
        while True:
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            print('script executing to scroll', scroll_attempt)
            sleep(5)
            curr_position = driver.execute_script("return window.pageYOffset;")
            print('curr_position',curr_position, last_position)
            if last_position == curr_position:
                scroll_attempt += 1
                if scroll_attempt >= 100:
                    print('scrolling attmps', scroll_attempt)
                    scrolling = False
                    break
                else:
                    sleep(2) 
            else:
                last_position = curr_position
                break
    ending_time = time.time()
    print('total time take', ending_time-starting_time)


# In[5]:


#             last_tweets = //div[@aria-label="Timeline: Dr. Taimur Rahman’s Tweets"]/div[1]/div[1]
import random

user_profession= ""
user_birthdate= ""
user_bio= ""
follower= ""
no_of_tweets= ""
username= ""
name= ""
location = ""
counter = 0

with open(f"test{random.randint(0,1999)}.csv", "wt", newline="",encoding='utf-8') as fp:
    writer = csv.writer(fp, delimiter=",")
    for i in data:
        website=f'https://twitter.com/{i}'
        print(website)
        driver.get(website)
        sleep(3)
        try:
            try:
                username = i
                print(username)
            except NoSuchElementException:
                username = ""
            try:
                name = driver.find_element_by_xpath('//div[@data-testid="UserName"]//span/span').text
    #                 print(name)
            except NoSuchElementException:
                name = ""
            try:
                location = driver.find_element_by_xpath('//span[@data-testid="UserLocation"]//span/span').text
    #                 print(location)   
            except NoSuchElementException:
                location = ""
            try:
                joined_data = driver.find_element_by_xpath('//span[contains(text(), "Joined")]').text
    #                 print(joined_data)
            except NoSuchElementException:
                joined_data = ""
            try:
                user_profession = driver.find_element_by_xpath('//span[@data-testid="UserProfessionalCategory"]//span//span').text
    #                 print(user_profession)     
            except NoSuchElementException:
                user_profession = ""
            try:
                user_birthdate = driver.find_element_by_xpath('//span[@data-testid="UserBirthdate"]').text
    #                 print(user_birthdate)
            except NoSuchElementException:
                user_birthdate= ""
            try:
                user_bio = driver.find_element_by_xpath('//div[@data-testid="UserDescription"]//span').text
    #                 print(user_bio)

            except NoSuchElementException:
                user_bio = ""
            try:
                follower = driver.find_element_by_xpath('//div[@data-testid="primaryColumn"]//div[1]/a[@dir="auto"][1]').text
    #                 print(follower)
            except NoSuchElementException:
                follower = ""
            try:
                following = driver.find_element_by_xpath('//div[@data-testid="primaryColumn"]//div[2]/a[@dir="auto"][1]').text
    #                 print(following) 
            except NoSuchElementException:
                following = ""
            try:
                no_of_tweets = driver.find_element_by_xpath('//div[contains(text(), "Tweets")]').text
    #                 print(no_of_tweets)
            except NoSuchElementException:
                no_of_tweets= ""
            print(i, username, name, location, joined_data,user_birthdate, user_profession, user_bio, follower, following, no_of_tweets)
            writer.writerow([i, username, name, location, joined_data,user_birthdate, user_profession, user_bio, follower, following, no_of_tweets])
          
        except Exception:
            print('exception ')



