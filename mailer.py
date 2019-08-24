#import packages
import sys
import os

#import methods
sys.path.append("./Functions/")
sys.path.append("./DB/")
sys.path.append("./GUI/")
from dependencyChecker import checkDependencies
from netSurfer import search 
from linkCollector import getLinks
from emailActivityChecker import checkActivity
from emailCollector import getEmails
from emailsender import sendEmail
from webdriver import getDriver
from progress import printProgressBar
from saveEmails import save2file

#Dependency Check
dependencies_check_result = checkDependencies()
if len(dependencies_check_result) > 0:
    for package in dependencies_check_result:
        print(package)
    exit()
    

keywords = input("Search Google: ")   #getquery is a function in searchingPanel that returns the query string

driver = getDriver()    #Create and Edit webdriver options
respond = search(keywords, driver)  #Search net for a keyword

links = getLinks(respond,printProgressBar)   #Get all the links from google search page

if len(links) <= 0:
    print("No links found")
    exit()

links = list(set(links))
email_list=[]

lc = 0
for link in links:
    lc += 1
    printProgressBar(lc, len(links), "Collecting Emails from each link","Completed")
    email_list = email_list + getEmails(link, driver)
driver.quit()

email_list = list(set(email_list))
emails = []
ec = 0
for email in email_list:
    ec += 1
    printProgressBar(ec, len(email_list), "Verifying Email Addresses","Completed")
    if checkActivity(email):
        emails.append(email)
save2file(emails, keywords)
        