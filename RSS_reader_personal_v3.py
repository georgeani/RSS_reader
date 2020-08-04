import feedparser
import os
import datetime
import time


# This is the most advanced scripts of them all, it allows you to save your favorite url, read them in the console
# or create a text file and read them there or both
# It also allows you to set up the config directory and files as well as a news directory

# Checks whether the needed directories exist
# If so it returns true else it returns false
def directories_exist():
    path1 = os.getcwd() + '\\config'
    print(path1)
    path2 = os.getcwd() + '\\News'
    suc = False

    if os.path.exists(path1) and os.path.exists(path2):
        suc = True

    if suc and os.listdir(path1) == [] and os.listdir(path2) == []:
        suc = False

    return suc


# This method creates the directories needed for the program to run
# The directories are created locally to where the program is located
def create_directories():
    path1 = os.getcwd() + '\\config'
    path2 = os.getcwd() + '\\News'

    try:
        os.mkdir(path1)
        os.mkdir(path2)
    except OSError:
        print('directory creation failed')
    else:
        print('directory creation worked')


# This method is used to collect the URLs in order for them to be then saved in the config file
def collect_urls():
    urls = []
    m = True
    while m:
        url = input('Please input the correct url, type q to exit')
        if url == 'q' or url == 'Q':
            m = False
        else:
            urls.append(url)
    return urls


# This method is used to create and update the config.txt file in the config directory
def create_config_file(news):
    path = os.getcwd() + '\\config\\config.txt'

    file = open(path, "w", encoding="utf-8")

    for new in news:
        file.write(new + "\n")
    file.close()


# This method is used to check whether the config file exist
def config_file_exists():
    path = os.getcwd() + '\\config\\config.txt'
    suc = False

    if os.path.exists(path) and os.path.isfile(
            path):
        suc = True

    return suc


# Loads the config file and outputs a list of all the URLs saved
def load_config():

    path = os.getcwd() + '\\config\\config.txt'
    with open(path, 'r') as f:
        news_urls = [line.strip() for line in f]

    return news_urls


# Shows all the headlines as well as saving them in the correct text file
def parser_saver_shower():
    urls = load_config()

    path = os.getcwd() + "\\News\\news" + str(datetime.date.today()) + ".txt"
    file = open(path, "w", encoding="utf-8")

    for url in urls:
        feed = feedparser.parse(url)
        entries = feed.entries

        for entry in entries:
            print(entry.published)
            file.write(entry.published + "\n")
            print("******")
            file.write("******" + "\n")
            print(entry.summary)
            file.write(entry.summary + "\n")
            print("------News Link--------")
            file.write("------News Link--------" + "\n")
            print(entry.link)
            file.write(entry.link + "\n")
            time.sleep(2)
    file.close()


# Saves all the headlines in the correct text file
def parser_saver():
    urls = load_config()

    path = os.getcwd() + "\\News\\news" + str(datetime.date.today()) + ".txt"
    file = open(path, "w", encoding="utf-8")

    for url in urls:
        feed = feedparser.parse(url)
        entries = feed.entries

        for entry in entries:
            file.write(entry.published + "\n")
            file.write("******" + "\n")
            file.write(entry.summary + "\n")
            file.write("------News Link--------" + "\n")
            file.write(entry.link + "\n")
    file.close()


# Main method, used to execute the program
if __name__ == "__main__":
    while True:
        if directories_exist() and config_file_exists():
            print("Choose whether you want: " + "\n")
            print("A. Reconfigure your sources" + '\n')
            print('B. Print the daily news in a text file' + '\n')
            print('C. Print the daily news in the console and text file' + '\n')
            print("Q. Exit program")
            com = input()

            if com == 'a' or com == 'A':
                sources = collect_urls()
                create_config_file(sources)
            elif com == 'b' or com == 'B':
                parser_saver()
            elif com == 'c' or com == 'C':
                parser_saver_shower()
            elif com == 'q' or com == 'Q':
                exit(0)
            else:
                print('This command is not recognizable')

        else:
            create_directories()
            sources = collect_urls()
            create_config_file(sources)
