from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

stop_word_set = set(stopwords.words('english'))|{'reuter'}


def normalize(raw_data):
    """The function to normalize each token list"""

    term_list = []
    token_list = raw_data
    ps = PorterStemmer()
    wnl = WordNetLemmatizer()
    for string in token_list:
        if validate_string(string):
            new_string = preprocess_string(string)
            if new_string not in stop_word_set:
                term_list.append(ps.stem(wnl.lemmatize(new_string)).encode('ascii', 'ignore'))
    return term_list


def validate_string(s):
    isvalid = False
    for char in s:
        if char.isdigit():
            isvalid = False
        elif char.isalpha():
            isvalid = True
    return isvalid


def preprocess_string(s):
    new_s = ""
    for char in s:
        if char.isalpha():
            new_s += char
    return new_s.lower()




# mylist = ["U.S.A.", "CAn't", "policemen", "^^.", "every-day", "games", "ab666", "Tony's", "daf", "fdfd"]
# normalizer = TokenNormalizer()
# print normalizer.normalize(mylist)





