import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://webscraper.io/test-sites/e-commerce/allinone/product/609'

headers = {"User-Agent":'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    #print(soup.prettify())

    price = soup.find_all("h4")[0].get_text()

    converted_price = float(price[1:5])

    if(converted_price > 1201.0):
        send_mail()

    print(converted_price)
    print(price)

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('mohdridhuan95@gmail.com','gcocrvgtyxzucfgu')

    subject = 'price fell down'
    body = 'check the link : https://webscraper.io/test-sites/e-commerce/allinone/product/609'

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
            'mohdridhuan95@gmail.com',
            'mohdridhuan95@gmail.com',
            msg
    )

    print('HEY EMAIL HAS BEEN SEND')

    server.quit()

while(True):
    check_price()
    time.sleep(60)
