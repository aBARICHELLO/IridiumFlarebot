import requests
import strings
import func
from bs4 import BeautifulSoup

def soup(bot, update, lat, lon):
    url = f'http://heavens-above.com/IridiumFlares.aspx?lat={lat}&lng={lon}&loc=Unspecified&alt=189&tz=EBST'
    req = requests.get(url).text
    soup = BeautifulSoup(req, 'html.parser')
    table = soup.find("table", {"class": "standardTable"})

    i = 0
    try:
        update.message.reply_text(strings.HEADER)
        for row in table.find_all("tr"):
            i+=1
            if i is 7:
                break
            if i is not 1:
                result = ""
                for cell in row.find_all("td"):
                    result += cell.find(text=True) + " | "
                update.message.reply_text(result)
    except AttributeError:
        update.message.reply_text("Daily quota reached")        
