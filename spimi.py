import sys
import os
import cPickle

memorySizeLimit = 512*1024
blockSizeLimit = 512
global DocID
DocID = 0
spimiFileNumber = 0
global endInput
endInput = False

def spimi_invert():
    """The SPIMI algorithm method to generate inverted-index"""

    global spimiFileNumber
    global endInput
    spimiFileNumber += 1
    filename = "inverted index/spimi" + str(spimiFileNumber) + ".txt"
    spimi_file = open(filename, "w")
    dictionary = {}
    input_stream = []

    while((memorySizeLimit - sys.getsizeof(dictionary))) >= blockSizeLimit:
        # Simulation of checking if the available memory is enough for the next block

        #print 'dictionary memory size is ' + str(sys.getsizeof(dictionary)) + ' byte'
        while len(input_stream) == 0:
            print 'file ID: ' + str(DocID)
            print 'dictionary memory size is ' + str(sys.getsizeof(dictionary)) + ' byte'
            input_stream = get_input()
        if input_stream == 'end':
            break
        token = input_stream.pop(0)
        term, doc_id = token[0], token[1]
        if term not in dictionary:
            postings_list = add_to_dictionary(dictionary, term)
        else:
            postings_list = get_postings_list(dictionary, term)
        add_to_postings_list(postings_list, doc_id)

    sorted_terms = []
    for k in sorted(dictionary):
        sorted_terms.append(k)
    # sorted_terms = sorted(dictionary, key=lambda postings: postings[0])
    write_to_disk(sorted_terms, dictionary, spimi_file)
    spimi_file.close()


def get_input():
    global DocID
    global endInput
    DocID += 1
    filename = 'file_terms/'+ str(DocID) + '.txt'
    if os.path.isfile(filename):
        with open(filename,'r') as fp:
            input_stream = cPickle.load(fp)
        fp.close
    else:
        endInput = True
        return 'end'
    return input_stream


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


# def merge_spimi_file():
#     rootdir = 'inverted index'
#     terms = []
#     dictionaries = []
#
#     for root, dirs, files in os.walk(rootdir):
#         if len(files) > 1:`         q
#             for doc in os.listdir(rootdir):
#                 if os.path.splitext(doc)[1] == '.txt':
#                     with open(doc,'r') as fp:
#                         terms.append(cPickle.load(fp))
#                         dictionaries.append(cPickle.load(fp))
#                     fp.close
#             for term_list in terms[1:]:
#                 for term in term_list:
#                     if term not in terms[0]:
#
#                         postings = get_postings_list(dictionaries[term_list.index], term)
#                         dictionaries[0][term]



def main1():
    if not os.path.isdir("inverted index"):
        os.mkdir("inverted index")
    while not endInput:
        print 'begin to generate time: ' + str(spimiFileNumber)
        spimi_invert()


def main2():
    ft = open('inverted index/spimi2.txt', 'r')
    mylist = read_from_dist(ft)
    mydic = read_from_dist(ft)
    for item in mylist:
        print item + ': ' + str(mydic[item])

def main3():
    ft = open('inverted index/spimi1.txt', 'r')
    mylist = read_from_dist(ft)
    mydic = read_from_dist(ft)
    print mylist
    print len(mylist)
    ft.close()


if __name__ == "__main__":
    main2()
