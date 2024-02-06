import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)

link = input("Enter the link of the webpage : ")
iterations = int(input("Enter the number of times you want the script to run : "))

for i in range(iterations):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(link)
   
    driver.close()
    