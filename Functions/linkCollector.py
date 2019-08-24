def getLinks(respond,printProgressBar):
    from bs4 import BeautifulSoup
    
    soup = BeautifulSoup(respond, 'lxml')
    links = soup.select('.rc .r a')
    link_storage = []
    pc = 0
    for link in links:
        pc += 1
        printProgressBar(pc,len(links),"Collecting Links from google", "Completed")
        temp = link.get('href')
        if len(temp) > 1:
            link_storage.append(temp)

    
    return link_storage