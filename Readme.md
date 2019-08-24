<p align="center">
  <img src="https://github.com/AkibSadmanee/mailfinder/blob/master/Fig/logo.png">
  <br>
  <h2 align="center">The Mail Finder</h2>
</p>

<p align="center">
  Search keywords in google, Get email addresses related to that keyword!! 
</p>

> Language Used: Python3 <br>

# The Dependency Packages:
* Selenium
* Bs4
* Re
* Lxml
* Smtplib
* Dns

# How To Use:
clone the repository to your local machine by using the following command in your terminal (Or just downlaod the project).
<br>
`git clone https://github.com/AkibSadmanee/Mailfinder.git`
<br>
Then just Run the "mailer.py" file with python3 :wink:
<br><br>
Use this command in the terminal to run the code.
<br>
`python3 mailer.py`
<br><br>
If you are in windows and python3 is set as the active python version then the following command will suffice.
<br>
`python mailer.py`
<br><br><br>
The crawled email addresses will appear in the <strong>"Emails"</strong> folder (Automatically generated). The filename will be the same as your search-keyword.
<br><br>
<h4>
If it doesn't work and throw error with Chromedriver, that means the chromedriver I have provided and the chrome version you have doesn't match. try downloading a chromedriver from the same version range of chrome that you have and replacing that with the provided chromedriver.
</h4>
Chromedrivers: https://chromedriver.chromium.org/downloads

<br><br>
<h3>Credits:</h3>
Email acitivity checker: https://www.scottbrady91.com/Email-Verification/Python-Email-Verification-Script

<h3>Warning about using this activity checker service</h3>
Warnings and Disclaimers
Whilst this process will get you up and running, you need to be aware of the following:
<ul>
  <li>Do this too much and you will get put on a naughty list (e.g. Spamhaus), especially if you are using a dynamic IP address from your ISP.</li>
  <li>B2C addresses: this does not work very well against the big boys who have their own procedures and spam rules (e.g.hotmail and yahoo).</li>
  <li>Incorrect results: some mail servers will give you incorrect results, for instance catch-all servers, which will accept all incoming email addresses, often forwarding incoming emails to a central mailbox. Yahoo addresses displays this catch-all behavior.</li>
</ul>
<h3>You may want to use VPN for the 1st warning</h3>
