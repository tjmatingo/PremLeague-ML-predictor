import requests
from playwright.sync_api import sync_playwright
import asyncio
from bs4 import BeautifulSoup

standings_url = "https://fbref.com/en/comps/9/Premier-League-Stats"


def scrape_fbref(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # or chromium
        context = browser.new_context()
        page = context.new_page()

        # Navigate to the page
        page.goto(url, timeout=60000)

        # Wait until the main content is loaded
        page.wait_for_selector("div#content", timeout=60000)

        # Get the HTML
        html = page.content()
        # html = await page.locator("table#stats_table").inner_html()
        browser.close()
    
    return html




cacheHandler = asyncio.run(scrape_fbref(standings_url)) 

data =  cacheHandler
print(data)
soup = BeautifulSoup(data, 'html.parser')

standings_table = soup.select('table.stats_table')[0]
# assigning all the a tags in the html pages to variable of a links 
links = standings_table.find_all('a')
