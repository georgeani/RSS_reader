import feedparser
import time

# This RSS reader script allows you to look at the feeds from all your favorite sites
# Here are some of mine
# It also prints the name of the websites you have chosen
print("Your personal daily review of news \n")

news = ["http://newsrss.bbc.co.uk/rss/newsonline_uk_edition/front_page/rss.xml",
        "http://newsrss.bbc.co.uk/rss/newsonline_uk_edition/business/rss.xml",
        "http://newsrss.bbc.co.uk/rss/newsonline_uk_edition/uk_politics/rss.xml",
        "http://newsrss.bbc.co.uk/rss/newsonline_uk_edition/technology/rss.xml",
        "http://newsrss.bbc.co.uk/rss/newsonline_uk_edition/world/rss.xml",
        "http://www.guardian.co.uk/rss/0,,,00.xml", "http://www.wired.com/news_drop/netcenter/netcenter.rdf",
        "https://www.kathimerini.gr/rss"]

websites = ["BBC frontpage", "BBC Business", "UK Politics", "BBC Tech", "BBC World News", "Guardian", "Wired",
            "Kathimerini"]

# prints the name of the website
# the titles and the news
m = 0
for new in news:
    print(websites[m] + "\n")
    feed = feedparser.parse(new)
    entries = feed.entries
    m = m+1

    for entry in entries:
        print(entry.published)
        print("******")
        print(entry.summary)
        print("------News Link--------")
        print(entry.link)
        time.sleep(2)
