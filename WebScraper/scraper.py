import requests
from bs4 import BeautifulSoup

# the page url we are scraping from 
standings_url = "https://fbref.com/en/comps/9/Premier-League-Stats"

# fetching all the data from the url link
data = requests.get(standings_url)

soup = BeautifulSoup(data.text, 'html.parser')

# get only the first element name in html page
standings_table = soup.select('table.stats_table')[0]


if standings_table:
    standings_table = standings_table[0]
    print(standings_table)
else:
    print("No stats_table found")


# assigning all the a tags in the html pages to a links variable  
links = standings_table.find_all('a')

# get all the links for each link 
links = [l.get("href") for l in links]

# all the squad links
links = [l for l in links if '/squad/' in l]


team_url = [f"https://fbref/com/{l}" for l in links]

