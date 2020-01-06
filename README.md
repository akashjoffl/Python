# Python
Learning Python for machine learning and web development

1. python.marcogg.com
2. mybinder.org // Online Python IDE

opensource@zone24x7.com

Contribute to Ornamentum (Angular)
https://ornamentum.app/

Add-Ons
1. Grammarly
2. Ghostery
3. PrivateX
4. Facebook Container
5. Tabby Cat

To get start with extensions -> https://webextensions.tech/

Slideshow -> http://slides.com/jenal/ots-srilanka

**********************

from requests import get

url = 'http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'

response = get(url)

print(response.text[:500])


