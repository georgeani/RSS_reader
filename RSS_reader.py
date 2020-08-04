import feedparser
import time

NewsFeed = feedparser.parse("http://newsrss.bbc.co.uk/rss/newsonline_uk_edition/front_page/rss.xml")

entries = NewsFeed.entries

for entry in entries:
    print(entry.published)
    print("******")
    print(entry.summary)
    print("------News Link--------")
    print(entry.link)
    time.sleep(2)
