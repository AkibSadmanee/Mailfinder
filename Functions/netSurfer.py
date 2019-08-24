def search(query_string_input, driver): 
    query_string = query_string_input.replace(' ','+')
    query_string = "https://www.google.com/search?q="+query_string
    
    driver.get(query_string)
    
    respond = driver.execute_script("return document.documentElement.outerHTML")
    return respond
