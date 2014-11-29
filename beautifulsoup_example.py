from bs4 import BeautifulSoup

# URL for package: http://www.crummy.com/software/BeautifulSoup/
# python3.4 setup.py install  - inside the beautiful soup folder

html_doc = """
<html><head><title>Hello world</title></head>
<body>
<p class="title"><b>Hello world</b></p>

<p class="story">With BeautifulSoup it's easy to work with HTML pages, such as a page that has:
<a href="http://google.com" class="google" id="google">Google</a>,
<a href="http://yahoo.com" class="yahoo" id="link2">Yahoo Search Engine</a> and
<a href="http://bing.com" class="bing" id="link3">Bing Site</a>;
You can grab any of them that you want!</p>

<p class="container">
    Other content goes here
</p>
"""

result = BeautifulSoup(html_doc)

print(result.title)
print(result.title.name)
print(result.a)
print(result.find_all('a'))
for link in result.find_all('a'):
    print(link.get('class'))


