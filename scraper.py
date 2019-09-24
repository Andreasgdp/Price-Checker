import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.pricerunner.dk/pl/110-4758227/Mus/Logitech-G502-Hero-Sammenlign-Priser'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}


def check_price():
  page = requests.get(URL, headers = headers)

  soup = BeautifulSoup(page.content, 'html.parser')


  title = soup.find("h1", {"class": "_2lZ6oyNnB-"}).get_text()

  price = soup.find("span", {"class": "_2cHLIqUS8H"}).get_text()

  price = int(price[:-3])

  if price <= 500:
    send_email(title, price)


def send_email(title, price):
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.ehlo()

  with open('key.key', 'r') as key:
    password = str(key.read())

  server.login('andreasgdp@gmail.com', password)

  subject = f'Price of {title} fell down'
  body = f'Check the link: {URL}'

  msg = f'Subject: {subject}\n\n{body}'

  server.sendmail(
    'andreasgdp@gmail.com',
    'andreasgdp@gmail.com',
    msg
  )
  server.quit()

check_price()