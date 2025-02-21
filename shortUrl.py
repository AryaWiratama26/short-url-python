import pyshorteners

def short_url(long_url):
    s = pyshorteners.Shortener()
    
    final_url = s.tinyurl.short(long_url)
    return final_url

