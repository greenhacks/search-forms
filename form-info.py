"""Use the Beautiful Soup and Requests libraries for web scraping"""
import requests
from bs4 import BeautifulSoup

# input = list of strings
# output = list of JSON

index = 0

# loop through all pages
while index >= 0:
    
    #get the page
    page = [requests.get("https://apps.irs.gov/app/picklist/list/priorFormPublication.html?indexOfFirstRow={index}&sortColumn=sortOrder&value=&criteria=&resultsPerPage=200&isDescending=false")]
    
    # create an instance of the BeautifulSoup class
    soup = BeautifulSoup(page.content, 'html.parser')

    # find the data that meets the requirements
    product_num = soup.find_all(class_="")
    title = soup.find_all()
    min_year = 0
    max_year = 0

    # print the data as JSON

    # increase the index by 200 (the max amount it can be increased)
    index += 200


