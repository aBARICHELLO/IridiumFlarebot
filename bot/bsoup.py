import requests
import strings
from bs4 import BeautifulSoup

def soup(bot, update, lat, lon):
    url = 'http://heavens-above.com/IridiumFlares.aspx?lat={}&lng={}&loc=Unspecified&alt=189&tz=EBST'.format(lat, lon)
    req = requests.get(url).text
    soup = BeautifulSoup(req, 'html.parser')
    table = soup.find("table", {"class": "standardTable"})

    i = 0
    try:
        update.message.reply_text(strings.HEADER)
        for row in table.find_all("tr"):
            i += 1
            if i is 7:
                break
            if i is not 1:
                result = ""
                j = 0
                for cell in row.find_all("td"):
                    result += strings.COLUMN[j] + cell.find(text=True) + "\n"
                    if j is 0: # Send the timestamp as a different message
                        update.message.reply_text(result)
                        result = ""
                    j += 1
                update.message.reply_text(result)
    except AttributeError:
        update.message.reply_text("Daily quota reached")

    update.message.reply_text(strings.REMIND_HELP)
