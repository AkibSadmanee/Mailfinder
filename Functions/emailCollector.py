def getEmails(link, driver): 
    import re
    import os
    
    #Go to the link
    try:
        driver.get(link)
        respond = driver.execute_script("return document.documentElement.outerHTML")
    except:
        respond = ""
    
    email_list=re.findall(r'[\w\.-]+@[\w\.-]+', respond)
    
    return email_list
