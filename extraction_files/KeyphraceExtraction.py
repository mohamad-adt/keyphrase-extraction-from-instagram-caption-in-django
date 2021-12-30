from pke.unsupervised import YAKE
from nltk.corpus import stopwords

extractor = YAKE()


################## LOAD CAPTION DOCUMENT #########################
def load_caption(document):
    extractor.load_document(input=document,
                            language='en',
                            normalization=None)


def set_stoplist():
    ################## SET STOPLIST AND WORD COUNT #####################
    stoplist = stopwords.words('english')
    extractor.candidate_selection(n=2, stoplist=stoplist)

    ################## CALCULATE SCORES FOR EXTRACTED KEYPHRASES ########
    extractor.candidate_weighting(window=2,
                                  stoplist=stoplist,
                                  use_stems=False)


def select_highest():
    ################## SELECT HIGHEST KEYPHRASES ######################
    key_phrases = extractor.get_n_best(n=10, threshold=0.8)
    return key_phrases


################## EXTRACT KEYPHRASES FROM TUPLE TO SHOW #########

def show_keypharses(key_phrases):
    key_phrases_WithoutScore = list()
    TupleToStr = list()
    Count = 0
    while (Count < len(key_phrases)):
        TupleToStr = list(key_phrases[Count])
        key_phrases_WithoutScore.append(TupleToStr[0])
        Count += 1
    return key_phrases_WithoutScore


def main(document):
    load_caption(document=document)
    set_stoplist()
    key_phrases = select_highest()
    key_phrase_WhithoutScore = show_keypharses(key_phrases=key_phrases)
    return key_phrase_WhithoutScore


if __name__ == '__main__':
    main(document=input('please enter dataset: '))
