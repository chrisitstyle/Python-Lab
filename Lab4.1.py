import urllib
x = urllib3.request.RequestMethods.urlopen(,)
urllib3.connection_from_url('https://www.google.com/').re
print(x.read())
# Example 2
URL2 = "http://pogoda.interia.pl/"
def doRequest(url):
#funkcja pomocnicza, która łączy się z zadanym adresem URL i zwraca zawartość strony
    return urllib3.request.RequestMethods.urlopen(url).read().decode()
def example1():
    print(doRequest(URL2))
# Example 2
with urllib3.request.RequestMethods.urlopen('http://www.python.org/') as f:
    print(f.read(300))
