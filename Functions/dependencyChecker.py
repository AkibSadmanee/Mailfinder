def checkDependencies(): 
    
    packages=[]
    try:
        import selenium
    except ImportError:
        packages.append('selenium not installed')
    
    try:
        import bs4
    except ImportError:
        packages.append('bs4 not installed')

    try:
        import re
    except ImportError:
        packages.append('re not installed')

    try:
        import lxml
    except ImportError:
        packages.append('lxml not installed')

    try:
        import smtplib
    except ImportError:
        packages.append('smtplib not installed')

    try:
        import dns
    except ImportError:
        packages.append('dnspython not installed')
   
    try:
        import tkinter
    except ImportError:
        packages.append('tkinter(3.x) not installed')
    
    return packages
