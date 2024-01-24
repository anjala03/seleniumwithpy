# from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
#driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get("https://www.geeksforgeeks.org/")
#driver.quit()


#from selenium.webdriver.chrome.service import Service
#from selenium import webdriver
#
#service = Service(executable_path="./chromedriver.exe")
#driver = webdriver.Chrome(service=service)
#driver.get("https://www.geeksforgeeks.org/")
#

from selenium import webdriver
driver= webdriver.Chrome()
driver.get("https://www.geeksforgeeks.org/")
driver.quit()