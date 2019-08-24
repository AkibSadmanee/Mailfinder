def checkActivity(email_address):    
    import re 
    import dns
    import smtplib
    from dns import resolver
    #Step 1: Check email
    #Check using Regex that an email meets minimum requirements, throw an error if not

    addressToVerify = email_address
    #match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)
    match = re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', addressToVerify)
    
    if match == None:
        return 0

    #Step 2: Getting MX record
    #Pull domain name from email address
    splitAddress=addressToVerify.split('@')
    domain=str(splitAddress[1])

    #get the MX record for the domain
    try:
        records = dns.resolver.query(domain, 'MX')
        mxRecord = records[0].exchange
        mxRecord = str(mxRecord)
    except:
        return 0
    #Step 3: ping email server
    #check if the email address exists

    # Get local server hostname


    # SMTP lib setup (use debug level for full output)
    server = smtplib.SMTP()
    server.set_debuglevel(0)

    # SMTP Conversation
    try:
        server.connect(mxRecord)
        server.helo(server.local_hostname)
        server.mail(email_address)
        code, message = server.rcpt(str(addressToVerify))
        server.quit()
    except:
        return 0
    # Assume 250 as Success
    if code == 250:
        return 1
    else:
        return 0

    try:    
        records = dns.resolver.query(domain, 'MX')
        mxRecord = records[0].exchange
        mxRecord = str(mxRecord)

        #Step 3: ping email server
        #check if the email address exists

        # Get local server hostname


        # SMTP lib setup (use debug level for full output)
        server = smtplib.SMTP()
        server.set_debuglevel(0)

        # SMTP Conversation
        server.connect(mxRecord)
        server.helo(server.local_hostname)
        server.mail(email_address)
        code, message = server.rcpt(str(addressToVerify))
        server.quit()

        # Assume 250 as Success
        if code == 250:
            return 1
        else:
            return 0
    except:
        return 0
