import requests
from bs4 import BeautifulSoup

# download the page
page = requests.get("https://apps.irs.gov/app/picklist/list/priorFormPublication.html")

# create an instance of the BeautifulSoup class
soup = BeautifulSoup(page.content, 'html.parser')

# pagination 

# loop through the output