from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# from db import Review
from selenium.common.exceptions import NoAlertPresentException
import csv
import re
import time

#read the csv file that contains the locations and the number of posts
with open('loc_data.csv', 'r') as f2:
    data = f2.read()
    new_data = data.splitlines()
    loc_lst = []
    num_disc_lst = []
    for i in range(0, 51):
        element = new_data[i].split(',')[0].replace(' ', '-').lower()
        loc_lst.append(element)
        element2 = new_data[i].split(',')[2]
        num_disc_lst.append(element2)
#Go to each location's URL
for i in range(0, 51):
    driver = webdriver.Chrome()
    url = 'https://community.whattoexpect.com/forums/%s.html' %(loc_lst[i])
    print(url)
                                                    
    driver.get(url)
    csv_file = open('%s.csv' %(loc_lst[i]), 'w', encoding='utf-8')
    writer = csv.writer(csv_file)

    #Obtain how many pages to scrape (depending on the number of posts)
    if int(num_disc_lst[i])%50==0:
        pages = int(num_disc_lst[i])//50
    else:
        pages = int(num_disc_lst[i])//50+1
    index = 1
    while index <= pages:
        counter = 0
        driver.get(url+'?page=%s' %str(index))
        try:
            print("Scraping Page Number: " + str(index))
            index += 1

            #Obtain post title (50 posts per page)
            while counter < 50:
                wait_post = WebDriverWait(driver, 99)
                posts = wait_post.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="topic-panel-container"]')))
                for post in posts:
                    post_dict = {}
                    try:
                    ### Find a title and number of replies per post
                        post_title = post.find_elements_by_xpath('//a[@class="topic-heading"]')[counter].text
                        num_replies = int(post.find_elements_by_xpath('//div[@class="topic-panel"]/a')[counter].text)
                    # print(post_title, num_replies)
                        counter+=1

                        post_dict['title'] = post_title
                        post_dict['num_replies'] = num_replies
                        writer.writerow(post_dict.values())

                    except:
                        post_title=""
                        num_replies=""
                        counter += 1
        
        except Exception as e:            
            print(e)
            csv_file.close()
            driver.close()
            break
    i += 1