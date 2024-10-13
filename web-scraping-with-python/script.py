# Import a scrapy Selector
from scrapy import Selector

# Import requests
import requests

url = "https://www.linkedin.com/search/results/people/?heroEntityKey=urn%3Ali%3Afsd_profile%3AACoAAB_L21UBaI8RoUqJNXOcC9IRb3dPG4RRfZ8&keywords=jonas%20nijssen&origin=SWITCH_SEARCH_VERTICAL&position=0&searchId=5efa1234-9f93-41a8-8d8a-a796d72af679&sid=a2)"
# Create the string html containing the HTML source
html = requests.get( url ).content

# Create the Selector object sel from html
sel = Selector( text = html )


"""
# Print out the number of elements in the HTML document
print( "There are 1020 elements in the HTML document.")
print( "You have found: ", len( sel.xpath('//*') ) )
"""
