'''This file is to generate inverted index using spimi according to terms list files'''

import sys
import os
import cPickle

memorySizeLimit = 0.5 * 1024 * 1024
blockSizeLimit = 512
# termfiledir = "Terms file by Sgmllib"
# targetdir = "inverted index 1"
# termfiledir = "Terms file by BS4"
# targetdir = "inverted index"
# termfiledir = "unfiltered terms"
# targetdir = "unfiltered inverted index"
# termfiledir = "no numbers terms"
# targetdir = "no numbers inverted index"
# termfiledir = "case folding terms"
# targetdir = "case folding inverted index"
# termfiledir = "30 stopwords terms"
# targetdir = "30 stopwords inverted index"
# termfiledir = "150 stopwords terms"
# targetdir = "150 stopwords inverted index"
termfiledir = "stemming terms"
targetdir = "stemming inverted index"

def spimi_invert():
    spimiFileNumber = 0
    DocID = 0
    endInput = False
    input_stream = []

    while not endInput:
        dictionary = {}
        while (memorySizeLimit - sys.getsizeof(dictionary)) >= blockSizeLimit:
            if input_stream ==[]:
                DocID += 1
                filename = termfiledir + '/' + str(DocID) + '.txt'
                if os.path.isfile(filename):
                    with open(filename, 'r') as termfile:
                        input_stream = read_from_dist(termfile)
                else:
                    endInput = True
                    break
                termfile.close()
            else:
                token = input_stream.pop(0)
                term, doc_id = token[0], int(token[1])
                if term not in dictionary:
                    postings_list = add_to_dictionary(dictionary, term)
                else:
                    postings_list = get_postings_list(dictionary, term)
                add_to_postings_list(postings_list, doc_id)
        sorted_terms = sort_terms(dictionary)
        # sorted_terms = sorted(dictionary, key=lambda postings: postings[0])
        spimiFileNumber += 1
        spimi_file = open(targetdir + "/spimi" + str(spimiFileNumber) + ".txt", 'w')
        write_to_disk(sorted_terms, dictionary, spimi_file)
        print 'Created file: ' + str(spimi_file)
        print 'Files processed: ' + str(DocID-1)
        spimi_file.close()


def merge_spimi_file():
    rootdir = targetdir
    terms = []
    dictionaries = []

    for root, dirs, files in os.walk(rootdir):
        if len(files) > 1:
            for doc in os.listdir(rootdir):
                if os.path.splitext(doc)[1] == '.txt':
                    with open(rootdir + '/' + doc, 'r') as fp:
                        terms.append(cPickle.load(fp))
                        dictionaries.append(cPickle.load(fp))
                    fp.close

            for index, term_list in enumerate(terms[1:]):
                print 'finished processing file: ' + str(index + 1)
                for term in term_list:
                    if term in terms[0]:
                        postings1 = dictionaries[0][term]
                        postings2 = dictionaries[index + 1][term]
                        new_postings = postings1 + postings2
                        dictionaries[0][term] = new_postings
                    else:
                        terms[0].append(term)
                        dictionaries[0][term] = dictionaries[index + 1][term]

            sorted_terms = sort_terms(dictionaries[0])
            fp = open(rootdir + '/FinalSpimi.txt', 'w')
            write_to_disk(sorted_terms, dictionaries[0], fp)
            fp.close()
        else:
            print 'Only 1 spimi file, no need to merge, please refer to:' + root + files


def add_to_dictionary(dictionary, term):
    dictionary[term] = []
    return dictionary[term]


def get_postings_list(dictionary, term):
    return dictionary[term]


def add_to_postings_list(postings_list, doc_id):
    if doc_id not in postings_list:
        postings_list.append(doc_id)


def write_to_disk(sorted_terms, dictionary, spimi_file):
    cPickle.dump(sorted_terms, spimi_file)
    cPickle.dump(dictionary, spimi_file)


def read_from_dist(spimi_file):
    spimi_obj = cPickle.load(spimi_file)
    return spimi_obj


def sort_terms(dict):
    sorted_terms = []
    for k in sorted(dict):
        sorted_terms.append(k)
    return sorted_terms


def begin_spimi():
    if not os.path.isdir(targetdir):
        os.mkdir(targetdir)
    spimi_invert()
    merge_spimi_file()


def create_readable_spimi_dictionary():
    fp = open(targetdir + '/FinalSpimi.txt', 'r')
    mylist = read_from_dist(fp)
    mydic = read_from_dist(fp)
    fp.close()
    with open('readable_dict.txt', 'w') as fw:
        for item in mylist:
            fw.write(item+': ' + str(mydic[item])+'\n')
            # print item + ': ' + str(mydic[item])
        fw.close


if __name__ == "__main__":
    begin_spimi()
