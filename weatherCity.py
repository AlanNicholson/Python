import re
import urllib.request
#http://www.weather-forecast.com/locations/Baile-Atha-Luain/forecasts/latest

city = input('Enter a City: ')
if str(city) == ('Athlone'):
    city=city.replace('Athlone' , 'Baile-Atha-Luain') 
    print(city)
    
weFor = 'http://www.weather-forecast.com/locations/'+city+'/forecasts/latest/'

data = urllib.request.urlopen(weFor).read()
dataD = data.decode("utf-8")

m = re.search('span class="phrase">',dataD)

bEgin = m.end()

fInish = bEgin +300

daWeather = dataD[bEgin:fInish]

n = re.search('</span></span></span>',daWeather)
fOOnish = n.start()

rEsult = daWeather[0:fOOnish]
rEsult = rEsult.replace('&deg;' , '\xB0')

print(rEsult)
