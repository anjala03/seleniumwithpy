from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import time
#elem = driver.find_elements(By.CLASS_NAME , "video-card-heading")
#for i in elem:
#    print(i.text)
#time.sleep(5)
#driver.get("https://www.google.com/")
#print(driver.title)
#time.sleep(5)
#driver.back()
#print(driver.title)

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()) , options=options)


driver.get("https://www.geeksforgeeks.org/")
print(driver.title)

elements= driver.find_elements(By.CLASS_NAME, "ant-col-offset-1" )
for element in elements: 
    heading= element.find_element(By.CLASS_NAME, "ant-col-23" )
    # heading= heading.find_element(By.CLASS_NAME, "video-card-heading")
    cards= element.find_elements(By.CLASS_NAME, "gfg_home_page_topic_card_cover" )
    # print(f"******** Heading= {heading.text} **********")
    for card in cards:
         subhead = card.find_element(By.CLASS_NAME, "ant-row" )
         print(f"The subheadings are: {subhead.text}")

driver.quit()




