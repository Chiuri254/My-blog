import requests

def get_quotes():

    url ='http://quotes.stormconsultancy.co.uk/random.json'
    response = requests.get(url)
    quote =response.json()

    return quote