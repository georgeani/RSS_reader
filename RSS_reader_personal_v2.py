import datetime
import feedparser
import time
import os

# This script is similar to personal_RSS_reader
# the difference is that it creates a text file or updates the previous one with all the headlines
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
path = os.getcwd() + "news" + str(datetime.date.today()) + ".txt"
text_file = open(path, "w", encoding="utf-8")
m = 0

# printing the name of the news outlet and saving it in the file as well as the headlines
for new in news:
    print(websites[m] + "\n")
    feed = feedparser.parse(new)
    entries = feed.entries
    m = m + 1

    text_file.write(websites[m] + "\n")
    for entry in entries:
        print(entry.published)
        text_file.write(entry.published + "\n")
        print("******")
        text_file.write("******" + "\n")
        print(entry.summary)
        text_file.write(entry.summary + "\n")
        print("------News Link--------")
        text_file.write("------News Link--------" + "\n")
        print(entry.link)
        text_file.write(entry.link + "\n")
        time.sleep(2)

text_file.close()
