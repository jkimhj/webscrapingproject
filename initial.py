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

#Go to the forum that is organized by "Locations" in the United States 
driver = webdriver.Chrome()
driver.get('https://community.whattoexpect.com/forums/united-states')

csv_file = open('initial.csv', 'w', encoding='utf-8')
writer = csv.writer(csv_file)

#Get all the locations, number of members, and the number of posts per location 
index = 1
while index <= 3: #3 pages of locations 
    counter = 0
    driver.get('https://community.whattoexpect.com/forums/united-states?page=%s' %str(index))
    
    try:
        print("Scraping Page Number: " + str(index))
        index += 1
        while counter < 24: # 24 locations per page
            wait_post = WebDriverWait(driver, 10)
            states = wait_post.until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="latest-stories-list"]/li[1]/a/div[2]/h3')))

            for state in states:
                state_dict = {}
                try:
                    ### Find a title and number of replies per post
                    state_title = state.find_elements_by_xpath('//h3[@class="groups-list__item__title"]')[counter].text
                    num_memb = state.find_elements_by_xpath('//small[1][@class="groups-list__item__info"]')[counter].text
                    num_memb = num_memb.split(' ', 1)[0]
                    
                    
                    # if num_memb[-1] == 'K':
                    #     num_memb = float(mystring[:-1])*1000
                    # else:
                    #     num_memb = num_memb
                    print(num_memb)
                    
                    num_disc = state.find_elements_by_xpath('//small[2][@class="groups-list__item__info"]')[counter].text
                    num_disc = int(re.search(r'\d+', num_disc).group())
                    # print(num_disc)
                    
                    state_dict['Location'] = state_title
                    state_dict['Members'] = num_memb
                    state_dict['Discussions'] = num_disc

                    writer.writerow(state_dict.values())
                    counter+=1
                except:
                    state_title=""
                    num_memb=""
                    num_disc=""
                    counter +=1

                    ### Locate the next button element on the page then call `button.click()` to click it.
        # button = driver.find_element_by_xpath('//a[@class="page-link next"]')
        # button.click()
        # time.sleep(2)
        
    except Exception as e:            
        print(e)
        csv_file.close()
        driver.close()
        break
        