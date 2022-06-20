# BoardGameGeek BoardGames Web Scraping

I made this project to learn how to use [Scrapy](https://scrapy.org/) framework with Python to perform web scraping.
The developed spider extracts all the board games from BoardGameGeek [website](https://boardgamegeek.com/) and exported into a csv file with the following data:

- Id
- Rank
- Name
- Url
- Rating
- Number of Votes
- Year
- Description
- Date

## Use Boardgamegeek XML API to scrape data details from boardgames
I use the following code [here](https://github.com/FilipeTheAnalyst/boardgames_xml_api/blob/master/boardgames/bgg_game_contents.py) to scrape data using XML API from Boardgamegeek website to get the following details for each game that was previously web scraped from their website:

- Thumbnail
- Language dependency
- Minimum number of players
- Maximum number of players
- Best player number
- Minimum playing time
- Maximum playing time
- Number of users rating the game
- Number of users that own the game
- Number of comments
- Number of votes for the weight of the game

### Prerequisites to run the project
Need to have installed the following Python packages:
1) scrapy
2) pandas
3) beautifulsoup4
