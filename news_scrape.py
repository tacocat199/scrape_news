# Import requests and BeautifulSoup libraries
import requests
from bs4 import BeautifulSoup

# Define a function that takes an article URL as input and returns the title and content
def scrape_article(url):
  # Send a GET request to the URL and get the response
  response = requests.get(url)
  # Check if the response status code is 200 (OK)
  if response.status_code == 200:
    # Parse the response content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")
    # Find the title element using its tag or class name (may vary depending on the website)
    title = soup.find("h1", class_="ArticleHeader__Heading")
    # Find the content element using its tag or class name (may vary depending on the website)
    content = soup.find("section", class_="ArticleContent zephr-article-content")
    # Check if both elements are found
    if title and content:
      # Return the text of the title and content elements
      return title.text, content.text
    else:
      # Return an error message if either element is not found
      return "Could not find title or content"
  else:
    # Return an error message if the response status code is not 200
    return "Invalid URL or server error"

# Test the function with an example article URL from New Scientist
url = "https://www.newscientist.com/article/2336385-korean-nuclear-fusion-reactor-achieves-100-millionc-for-30-seconds/"
result = scrape_article(url)
if isinstance(result, tuple):
    title, content = result
    print("Title:", title)
    print("Content:", content)
else:
    print(result)

