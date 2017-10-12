from bs4 import BeautifulSoup
import os

#D:/concordia study/Term 6 COMP 6791 Information Retrival/Lab/reuters/reut2-000.sgm
# with open("D:/concordia study/Term 6 COMP 6791 Information Retrival/Lab/reuters/reut2-000.sgm") as fp:
#     soup = BeautifulSoup(fp, 'html.parser')
# #article = soup.reuters
# # title = article.title
# # body = article.body
# # print article['newid']
# # print title.string
# # print body.string
#
# for article in soup.find_all('reuters'):
#     for tag in article.find_all():
#         if tag.name == 'title' or tag.name == 'body':
#             print tag.string


def parse(filepointer):

    soup = BeautifulSoup(filepointer, 'html.parser')
    for article in soup.find_all('reuters'):
        filename = "articles/" + article['newid'] + ".txt"
        doc_file = open(filename, "w")
        for tag in article.find_all():
            if tag.name == 'title':
                doc_file.write(tag.string + "\n")
            elif tag.name == 'body':
                doc_file.write(tag.string.encode('utf-8'))
        doc_file.close()


if not os.path.isdir("articles"):
    os.mkdir("articles")
# Parse the file and output the results
rootdir = 'D:/concordia study/Term 6 COMP 6791 Information Retrival/Lab/reuters/'
for doc in os.listdir(rootdir):
    if os.path.splitext(doc)[1] == '.sgm':
        ft = open(os.path.join(rootdir, doc))
        print ft
        parse(ft)
        ft.close()

# ft = open("D:/concordia study/Term 6 COMP 6791 Information Retrival/Lab/reuters/reut2-017.sgm")
# parse(ft)
# ft.close()
