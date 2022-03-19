from lib.parsers.data_parsers.data_parser import DataParser
from types_.inn import Inn
from types_.contacts import Contacts
import aiohttp
from bs4 import BeautifulSoup

HEADERS = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:97.0) Gecko/20100101 Firefox/97.0' }

class ContactsParser(DataParser):
    async def parse(self, inn: Inn):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://www.list-org.com/search?type=inn&val={inn}', headers=HEADERS) as response:
                    text = await response.text()
                    soup = BeautifulSoup(text)
                    href = soup.select_one('a[href^="/company"]')['href']
                    async with session.get(f'https://www.list-org.com{href}', headers=HEADERS) as response:
                        text = await response.text()
                        soup = BeautifulSoup(text)
                        phone = getattr(soup.select_one('a[href^="/phone"]'), "text", None)
                        email = getattr(soup.select_one('a[href^="mailto:"]'), "text", None)
                        return Contacts(phone=phone, email=email).dict()
        except Exception as e:
            print(inn, e)
            return Contacts(phone=None, email=None).dict()  
