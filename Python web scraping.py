from bs4 import BeautifulSoup
import requests

# using request to get the website
# .get will return a response object, .text will get the source code
source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source,'lxml')

# print all the formated code form the website
# print(soup.prettify())




# work on the first article first


# print out the html code for the first article
# article = soup.find('article')
# print(article.prettify())

# print the headline, the date part and the paragraph. h2, p, and div.p is the html code.
# headline = article.h2.a.text
# summary = article.p.text
# .p is the first p in that section
# summary2 = article.find('div',class_='entry-content').p.text
#summary2=article.div.p.text also returns that paragraph
# print(headline)
# print(summary)
# print(summary2)

# 'iframe', class_='youtube-player' and src, is the html code. with the dictionary it will return the embeded link to that video
# vid_src = article.find('iframe', class_='youtube-player')['src']
# print(vid_src)
# http://www.youtube.com/embed/-aKFBoZpiqA?version=3&rel=1&fs=1&autohide=2&showsearch=0&showinfo=1&iv_load_policy=1&wmode=transparent

# get the video id from this link, if split the link by '/', the video id should be in index 4
# vid_id = vid_src.split('/')[4]
# print(vid_id )
# -aKFBoZpiqA?version=3&rel=1&fs=1&autohide=2&showsearch=0&showinfo=1&iv_load_policy=1&wmode=transparent

# the video id is the part before the questions mark
# vid_id = vid_id.split('?')[0]
#print(vid_id )
# aKFBoZpiqA


# using f to do a formated string
# yt_link = f'https://youtube.com/watch?v={vid_id}'
# print(yt_link)
# https://youtube.com/watch?v=-aKFBoZpiqA


# save the info into a csv file
csv_file = open('Web_Scraping.csv', 'w')
csv_writer = csv.writer(csv_file)
#give name to each column
csv_writer.writerow(['Headline', 'Summary', 'Link'])

# Now lets work on all the articles on that page
for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    # in case some sections do not have a video
    try:
     vid_src = article.find('iframe', class_='youtube-player')['src']
     vid_id = vid_src.split('/')[4]
     vid_id = vid_id.split('?')[0]
     yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link=None

    print(yt_link,'\n')



# great

