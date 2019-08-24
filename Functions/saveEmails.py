def save2file(emails,keywords):
    import os
    if not os.path.exists('Emails'):
        os.makedirs('Emails')
    filename = keywords.strip().replace(" ","_")
    filepath = "./Emails/" + filename + ".txt"
    fw = open(filepath,"w+")
    for email in emails:
        fw.writelines(email)
        fw.writelines("\n")
    fw.close()
