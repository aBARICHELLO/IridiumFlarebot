import requests
from bs4 import BeautifulSoup

def soup(bot, update, lat, lon):
    url = f'http://heavens-above.com/IridiumFlares.aspx?lat={lat}&lng={lon}&loc=Unspecified&alt=189&tz=EBST'
    req = requests.get(url).text
    soup = BeautifulSoup(req, 'html.parser')
    table = soup.find("table", {"class": "standardTable"})
    
    for row in table.find_all("tr"):
        result = ""
        for cell in row.find_all("td"):
            result += cell.find(text=True) + " "
        result.replace("[\r\n\t", "")    
        update.message.reply_text(result)
