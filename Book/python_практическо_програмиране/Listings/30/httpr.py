from urllib import request, parse
# URL, към който се осъществява достъп 
url = 'http://example.com/script.php'
# Словарь с параметрами запроса (если есть)
parms = {
  'var1' : 'value1',
  'var2' : 'value2'
}
# Кодираме заявката
querystring = parse.urlencode(parms)

# Осъществяваме GET-заявка и четем отговора
u = request.urlopen(url+'?' + querystring)
resp = u.read()
