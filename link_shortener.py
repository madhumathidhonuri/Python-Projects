import pyshorteners
'''
pyshorteners is a Python library that provides a simple and unified way to use different URL shortening services (like Bitly, TinyURL, etc.). 
It acts as a wrapper around these services, making it easy to shorten and expand URLs in your Python programs.
'''
link=input("Enter the Link: ")

shortener=pyshorteners.Shortener() #Shortener(): This is a class in the library that provides access to various URL shortening services.

shortened_link = shortener.tinyurl.short(link)
#.tinyurl: Accesses the TinyURL service from the available shortening services in pyshorteners.
#.short(link): Calls the short() method to shorten the URL given in link.

print("Shortened Link:",shortened_link)

