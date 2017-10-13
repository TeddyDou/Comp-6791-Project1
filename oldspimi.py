import sys
import os
import cPickle

memorySizeLimit = 0.5*1024*1024
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

    sorted_terms = sort_terms(dictionary)

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


def sort_terms(dict):
    sorted_terms = []
    for k in sorted(dict):
        sorted_terms.append(k)
    return sorted_terms


def merge_spimi_file():
    rootdir = 'inverted index'
    terms = []
    dictionaries = []

    for root, dirs, files in os.walk(rootdir):
        if len(files) > 1:
            for doc in os.listdir(rootdir):
                if os.path.splitext(doc)[1] == '.txt':
                    with open(rootdir+'/'+doc,'r') as fp:
                        terms.append(cPickle.load(fp))
                        dictionaries.append(cPickle.load(fp))
                    fp.close

            for index, term_list in enumerate(terms[1:]):
                print term_list, index+1
                for term in term_list:
                    if term in terms[0]:
                        postings1 = dictionaries[0][term]
                        postings2 = dictionaries[index+1][term]
                        new_postings = postings1 + postings2
                        dictionaries[0][term] = new_postings
                    else:
                        terms[0].append(term)
                        dictionaries[0][term] = dictionaries[index+1][term]

            sorted_terms = sort_terms(dictionaries[0])
            fp = open('inverted index/FinalSpimi.txt','w')
            write_to_disk(sorted_terms, dictionaries[0], fp)
            fp.close()
        else:
            print 'Only 1 spimi file, no need to merge, please refer to:' + root + files


def main1():
    if not os.path.isdir("inverted index"):
        os.mkdir("inverted index")
    while not endInput:
        print 'begin to generate time: ' + str(spimiFileNumber)
        spimi_invert()

def main6():
    if not os.path.isdir("inverted index"):
        os.mkdir("inverted index")
    print 'begin to generate time: ' + str(spimiFileNumber)
    spimi_invert()
    print DocID

def main2():
    ft = open('inverted index/FinalSpimi.txt', 'r')
    mylist = read_from_dist(ft)
    mydic = read_from_dist(ft)
    for item in mylist:
        print item + ': ' + str(mydic[item])

def main3():
    ft = open('inverted index/spimi1_MM1.txt', 'r')
    mylist = read_from_dist(ft)
    mydic = read_from_dist(ft)
    print mylist
    print len(mylist)
    ft.close()

def main4():
    merge_spimi_file()

def main5():
    # file1 = open('inverted index/spimi1_MM1.txt', 'r')
    # file2 = open('inverted index V01/FinalSpimi.txt', 'r')
    # mylist1 = read_from_dist(file1)
    # mydict1 = read_from_dist(file1)
    # mylist2 = read_from_dist(file2)
    # mydict2 = read_from_dist(file2)
    # file1.close()
    # file2.close()
    # list3 = list(set(mylist1) - set(mylist2))
    # print list3
    # print mydict1[list3[0]]

    '''['westard'], [u'7916']'''

    rootdir = 'inverted index V01'
    for doc in os.listdir(rootdir):
        if os.path.splitext(doc)[0] == 'spimi*':
            ft = open(os.path.join(rootdir, doc))
            l = read_from_dist(ft)
            if 'westard' in l:
                print doc

if __name__ == "__main__":
    main6()
