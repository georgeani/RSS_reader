import feedparser
import time

# This script allows you to input the RSS feed that you want to receive information from
# all the titles will be then be printed
feed = input("input your feed")

NewsFeed = feedparser.parse(feed)

entries = NewsFeed.entries

for entry in entries:
    print(entry.published)
    print("******")
    print(entry.summary)
    print("------News Link--------")
    print(entry.link)
    time.sleep(2)
