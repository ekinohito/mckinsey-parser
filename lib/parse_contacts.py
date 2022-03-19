from typing import Iterable, List, Tuple
import aiohttp
from types_.inn import Inn
from types_.contacts import Contacts
from bs4 import BeautifulSoup

HEADERS = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:97.0) Gecko/20100101 Firefox/97.0' }

async def parse_contacts(inns: List[Inn]) -> Iterable[Tuple[Inn, Contacts]]:
    try:
        async with aiohttp.ClientSession() as session:
            for inn in inns:
                try:
                    async with session.get(f'https://www.list-org.com/search?type=inn&val={inn}') as response:
                        text = await response.text()
                        soup = BeautifulSoup(text)
                        href = soup.select_one('a[href^="/company"]')['href']
                        async with session.get(f'https://www.list-org.com{href}') as response:
                            text = await response.text()
                            soup = BeautifulSoup(text)
                            phone = getattr(soup.select_one('a[href^="/phone"]'), "text", None)
                            email = getattr(soup.select_one('a[href^="mailto:"]'), "text", None)
                            yield (inn, Contacts(phone=phone, email=email))
                except Exception as e:
                    print(inn, e)
                    yield (inn, Contacts(phone=None, email=None))
    except Exception as e:
        print(e)
