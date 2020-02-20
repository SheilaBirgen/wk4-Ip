
import urllib.request, json
from .models import Quote

base_url = None

def configure_request(app):
    global base_url
    base_url = app.config['API_BASE_URL']
    
def get_quotes():
    
    get_quotes_url = base_url.format
    print(get_quotes_url)
    
    with urllib.request.urlopen('http://quotes.stormconsultancy.co.uk/random.json') as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)
        
        return get_quotes_response

    
    
    
    
    
    
    
    
    
    
    
    
    # # response = requests.get(url).json()
    # response = get(url).json()
    # random_quote=Quote(response.get("author"),response.get("quote")) 
    # return random_quote