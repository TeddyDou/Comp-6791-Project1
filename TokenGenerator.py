from bs4 import BeautifulSoup
import os
import nltk
import newTokenNormalizer
import cPickle
import spimi


def parse_file(filepointer):

    soup = BeautifulSoup(filepointer, 'html.parser')
    for article in soup.find_all('reuters'):
        doc_id = article['newid']
        #doc_file = open(filename, "w")
        article_string = ""
        for tag in article.find_all():
            if tag.name == 'text'and not tag.attrs == {}:
                if tag['type'] == 'UNPROC':
                    article_string += tag.string
                elif tag['type'] == 'BRIEF':
                    article_string += tag.title.string
                break
            if tag.name == 'title':
                article_string += tag.string+'\n'
            elif tag.name == 'body':
                article_string += tag.string
        if article_string.__len__() == 0:
            print "The article with error is " + doc_id
        terms = generate_terms(article_string.encode('utf-8'))
        tokens = []
        for term in terms:
            tokens.append([term, doc_id])
        if not os.path.isdir("file_terms"):
            os.mkdir("file_terms")
        filename = "file_terms/" + doc_id + ".txt"
        f = open(filename, "w")
        cPickle.dump(tokens, f)
        f.close()
        print "Finish processing file " + doc_id


def generate_terms(string):
    tokens = nltk.word_tokenize(string)
    terms = newTokenNormalizer.normalize(tokens)
    return terms

rootdir = 'D:/concordia study/Term 6 COMP 6791 Information Retrival/Lab/reuters/'
filepath = 'D:/concordia study/Term 6 COMP 6791 Information Retrival/Lab/reuters/reut2-000.sgm'
filepath2 = 'articles/1.txt'
for doc in os.listdir(rootdir):
    if os.path.splitext(doc)[1] == '.sgm':
        ft = open(os.path.join(rootdir, doc))
        parse_file(ft)
        ft.close()
# if not os.path.exists("file_terms"):
#     os.makedirs("file_terms")
# ft = open(filepath)
# parse_file(ft)
# ft.close()

# myfile = open('file_terms/2.txt')
# spimi_obj = cPickle.load(myfile)
# print spimi_obj

# f = open(filepath2)
# s = f.read()
# docid = 1
# a = generate_tokens(s)
# tokens = []
# for term in a:
#     tokens.append([term, docid])
# for b in tokens:
#     print b[1]

