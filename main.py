import bs4
import requests
from Email import Email
class PriceTracker:
    def __init__(self,URL):
        self.URL = URL

    def find_price(self):
        try:
            res = requests.get(self.URL, headers={"User-Agent": "Defined"})
            soup = bs4.BeautifulSoup(res.text, 'html.parser')
        except:
            return
        try:
            if 'flipkart' in self.URL:
                price = soup.find(class_='_30jeq3 _16Jk6d')
                price = price.get_text().replace(',', '').replace('₹', '')
                price = float(price)
                return price
            elif 'amazon' in self.URL:
                try:
                    price = soup.find(id='priceblock_ourprice')
                    price = price.get_text().replace(',', '').replace('₹', '')
                    price = float(price)
                    return price
                except:
                    price = soup.find(id='priceblock_dealprice')
                    price = price.get_text().replace(',', '').replace('₹', '')
                    price = float(price)
                    return price
        except:
               return
        return


    def find_title(self):
        try:
            res = requests.get(self.URL, headers={"User-Agent": "Defined"})
            soup = bs4.BeautifulSoup(res.text, 'html.parser')
        except:
            return
        try:
            if 'flipkart' in self.URL:
                title = soup.find(class_ = 'B_NuCI')
                return title.get_text().strip()
            elif 'amazon' in self.URL:
                title = soup.find(id='productTitle')
                return title.get_text().strip()
        except:
            return
        return


if __name__ == '__main__':
    URL = input('Enter URL of product(flipkart/Amazone) : ')
    product = PriceTracker(URL)
    price = product.find_price()
    title = product.find_title()
    if price == None:
        print('Invalid link!')
    else:
        print('Product: ',title)
        print('Price: ',price)

    key = input('Do you want to receive Email notification for falling price?(1/0) ')
    while key == '1':
        email = input('Enter your Email: ')
        e = Email(email,title,price,URL)
        send = e.send_email()
        if send==-1:
            print('Invalid email! Try again')
        else:
            key = '0'


