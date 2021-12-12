from nltk import pos_tag, RegexpParser
from nltk.tokenize import PunktSentenceTokenizer, word_tokenize

# import text of choice here
text = open("/home/cristina/Documents/py-files/language-parsing/dorian-gray.txt",encoding='utf-8').read().lower()

#word or sentence tokenizer:

def word_sentence_tokenize(text):
    sentence_tokenizer = PunktSentenceTokenizer(text)
    sentence_tokenized = sentence_tokenizer.tokenize(text)
    word_tokenized = list()
    for tokenized_sentence in sentence_tokenized:
        word_tokenized.append(word_tokenize(tokenized_sentence))
    return word_tokenized

# sentence and word tokenize text here
word_tokenized_text = word_sentence_tokenize(text)

# store and print any word tokenized sentence here
single_word_tokenized_sentence = word_tokenized_text[104]
# print(single_word_tokenized_sentence)


# create a list to hold part-of-speech tagged sentences here
pos_tagged_text = list()

# create a for loop through each word tokenized sentence here
for sentence in word_tokenized_text:
  # part-of-speech tag each sentence and append to list of pos-tagged sentences here
  pos_tagged_text.append(pos_tag(sentence))

# store and print any part-of-speech tagged sentence here
single_pos_sentence = pos_tagged_text[100]
# print(single_pos_sentence)


# define noun phrase chunk grammar here
np_chunk_grammar = "NP: {<DT>?<JJ>*<NN>}"

# create noun phrase RegexpParser object here
np_chunk_parser = RegexpParser(np_chunk_grammar)

# define verb phrase chunk grammar here
vp_chunk_grammar = "VP: {<DT>?<JJ>*<NN><VB.*><RB.?>?}"

# create verb phrase RegexpParser object here
vp_chunk_parser = RegexpParser(vp_chunk_grammar)


# create a list to hold noun phrase chunked sentences and a list to hold verb phrase chunked sentences here
np_chunked_text = []
vp_chunked_text = []


# create a for loop through each pos-tagged sentence here
for sentence in pos_tagged_text:
  # chunk each sentence and append to lists here
  np_chunked_text.append(np_chunk_parser.parse(sentence))
  vp_chunked_text.append(vp_chunk_parser.parse(sentence))

#use a counter to determine most common chunks
from collections import Counter

def np_chunk_counter(chunked_sentences):
    chunks = []
    for chunked_sentence in chunked_sentences:
        for subtree in chunked_sentence.subtrees(filter=lambda t: t.label() == 'NP'):
            chunks.append(tuple(subtree))
    chunk_counter = Counter()
    for chunk in chunks:
        chunk_counter[chunk] += 1
    return chunk_counter.most_common(30)

def vp_chunk_counter(chunked_sentences):
    chunks = []
    for chunked_sentence in chunked_sentences:
        for subtree in chunked_sentence.subtrees(filter=lambda t: t.label() == 'VP'):
            chunks.append(tuple(subtree))
    chunk_counter = Counter()
    for chunk in chunks:
        chunk_counter[chunk] += 1
    return chunk_counter.most_common(30)

# # store and print the most common NP and VP chunks here

print("Most common noun-phrases")
for chunk in np_chunk_counter(np_chunked_text):
    print(chunk)
    print("")

print("Most common verb-phrases")
for chunk in vp_chunk_counter(vp_chunked_text):
    print(chunk)
    print("")