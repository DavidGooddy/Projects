from ast import Import
from cmath import log
from email import message
#Imports email / stores account and passwords
import json
import smtplib
from socket import MsgFlag
import urllib.request

# imports code used to interact with website
from datetime import datetime
from bs4 import BeautifulSoup
from email.message import EmailMessage, Message


def check_availability(url):
    global log
    try:
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, features='html.parser')
        if phrase in soup.text:
            return False
            return True
    
    except:
        log += ('Error parsing the website')
    
    
    def main():
        url = 'https://www.swatch.com/en-gb/mission-to-uranus-so33l100/SO33L100.html'
        phrase = 'Mission to uranus in stock'
        available = check_availability(url, phrase)
        
    if available:
        
       msg = EmailMessage()
       msg = ['subject'] = 'Omega Swatch now in stock'
       msg = ['from'] =
       msg = ['To'] = 
        
        
    