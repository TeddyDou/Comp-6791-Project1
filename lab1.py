import nltk
import TokenNormalizer
import os
from cPickle import HIGHEST_PROTOCOL,dump,load


# filename = "articles/2.txt"
# f = open(filename, "r")
# s = f.read()
# article_id = os.path.splitext(os.path.basename(f.name))[0]
# print article_id
#
#
# # Create a text directory if one does not exist
# a = nltk.word_tokenize(s)
# normalizer = TokenNormalizer.TokenNormalizer()
# token_stream = normalizer.normalize(a)



# source = "articles/2.txt"
mylist = ['carl', 'good', 'ted', 'beth']
listlist = [['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l'], ['m', 'n', 'o', 'p']]
list2d = [[1,2,3],[4,5,6], [7], [8,9]]

mylist1 = ['carl', 'alan', 'bob', 'danny']
mylist2 = ['carl', 'adam', 'bob', 'fenir']
mylist3 = ['eve', 'alan', 'sven', 'fenir']

mydict1 = {'carl': [40, 86, 93],
          'alan': [2, 53],
          'bob': [1, 9],
          'danny': [3]}
mydict2 = {'carl': [23, 56, 46],
          'adam': [4, 73],
          'bob': [3, 22],
          'fenir': [9, 36, 41, 105]}
mydict3 = {'eve': [15, 88],
          'alan': [6, 43],
          'sven': [1, 87],
          'fenir': [69, 105]}

dicts = []
dicts.append(mydict1)
dicts.append(mydict2)
dicts.append(mydict3)

lists = []
lists.append(mylist1)
lists.append(mylist2)
lists.append(mylist3)

for term_list, index in enumerate(lists[1:]):
    print term_list, index
    for term in term_list:
        if term in lists[0]:
            postings1 = dicts[index][term]
            postings2 = dicts[0][term]
            newpostings = postings1 + postings2
            dicts[0][term] = newpostings
        else:
            lists[0].append(term)
            dicts[0][term] = dicts[term_list.index][term]

print term[0]
print dicts[0]

# ints = [8, 23, 45, 12, 78]
# for idx, val in enumerate(ints):
#     print(idx, val)

# [{'bob': [1, 9], 'danny': [3], 'alan': [2, 53], 'carl': [40, 86, 93]},
#  {'bob': [3, 22], 'adam': [4, 73], 'carl': [23, 56, 46], 'fenir': [9, 36, 41, 105]},
#  {'sven': [1, 87], 'eve': [15, 88], 'alan': [6, 43], 'fenir': [69, 105]}]



# sorted_terms = sorted(mydict, key=lambda postings: postings[0])
# print mydict
# print sorted_terms

# student_tuples = [
#         ('john', 'A', 15),
#         ('jane', 'B', 12),
#         ('dave', 'B', 10),
# ]
