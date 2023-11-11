def rss_reader(url):
    from urllib.request import urlopen
    from xml.etree.ElementTree import parse

    # Зареждаме RSS-лента и я парсваме
    u = urlopen(url)
    doc = parse(u)
    # Извличаме и показваме интересуващите ни тагове
    for item in doc.iterfind('channel/item'):
        title = item.findtext('title')
        date = item.findtext('pubDate')
        link = item.findtext('link')

        print(title)
        print(date)
        print(link)
        print()

rss_reader('http://www.dkws.org.ua/phpbb2/rss.php')
