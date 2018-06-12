import bs4 as bs
import urllib.request


def compute_exchange_rate():
    url = 'http://e-consulta.sunat.gob.pe/cl-at-ittipcam/tcS01Alias'
    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source, 'lxml')
    table = soup.find('table', class_='class="form-table"')
    table_rows = table.find_all('tr')
    count = 0
    list = []
    for tr in table_rows:
        count = count + 1
        if count > 1:
            td = tr.find_all('td')
            list = [i.text.strip() for i in td]
    position = int((len(list) - 3))
    list_er = list[position:]
    exchange_rate = {
        u'day': ''.join(list_er[:1]),
        'purchase': ''.join(list_er[1:2]),
        'sale': ''.join(list_er[2:3])
    }
    return exchange_rate
