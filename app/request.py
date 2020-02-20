
import urllib.request, json
from .models import Quote

def get_quote():
    url="http://quotes.stormconsultancy.co.uk/random.json"
    
    with urllib.request.urlopen(url) as url:
        quote_data=url.read()
        quote_response=json.loads(quote_data)
        return quote_data

    
    if quote_data:
        author = quote_data.author 
        quote = quote_data.quote 
    
    rand_quote = Quote(author, quote)

    return rand_quote
    
    
    
    
    
    
    
    
    
    
    
    
    # # response = requests.get(url).json()
    # response = get(url).json()
    # random_quote=Quote(response.get("author"),response.get("quote")) 
    # return random_quote