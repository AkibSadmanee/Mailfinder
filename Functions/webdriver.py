def getDriver():
    from selenium import webdriver
    import os
    if os.name == 'nt':
        chrome_path= r"./chromedriver_windows/chromedriver.exe"
    else:
        chrome_path= r"./chromedriver_linux/chromedriver"

    chrome_options = webdriver.ChromeOptions()  
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(chrome_path,chrome_options=chrome_options)    
    
    driver.set_window_size(0,0)
    driver.set_window_position(15000,15000)
    return driver