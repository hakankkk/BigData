#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
import nltk
from os.path import join
import os, re, pprint, types, copy, math, sys, hashlib
import numpy as np

try:
    import mmh3 as mmh3
except ImportError:
    import mmh3_py as mmh3

from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import *

reload(sys)
sys.setdefaultencoding('utf8')

def tokenize_text(input_text):

	# print 'Tokenizing text...\n'

	input_text = input_text.replace('“'.decode('utf-8'), '"')
	input_text = input_text.replace('”'.decode('utf-8'), '"')
	input_text = input_text.replace('‘'.decode('utf-8'), '\'')
	input_text = input_text.replace('’'.decode('utf-8'), '\'')

	input_text = re.findall(r'([a-zA-Z0-9_]+\-[a-zA-Z0-9_]+|[a-zA-Z0-9_]+)', input_text.lower())
	# input_text = word_tokenize(input_text.lower())

	stop_words = stopwords.words('english')
	input_text = [w for w in input_text if w not in stop_words]

	print input_text

	return input_text

def stem_text(input_text):

	# print 'Stemming tokens...\n'

	stemmer = PorterStemmer()
	stemmed = []
	
	for w in input_text:
		stemmed.append(stemmer.stem(w))

	return stemmed


def shingler(input_text, preprocess, k, seed):

	if preprocess:
		input_text = tokenize_text(input_text)
		input_text = stem_text(input_text)

	shingles = set()

	# print 'Generating shingles...\n'

	for i in xrange(len(input_text) - k + 1):
		shingle = ' '.join(input_text[i: i+k])
		shingles.add(np.uint32(mmh3.hash(shingle, seed)))

	return list(shingles)

def generate_output(input_file, output_path, dates, preprocess=True, shingle_size=3, hash_seed=1234):
	with openinput_file as infile:
    for doc in infile:
    	json_input = json.loads(doc)
    	if content not in json_input or published not in json_input or id not in json_input:
    		continue

    	if json_input['published'] not in dates:
    		continue

    	doc_content = json_input['content']

    	doc_id = json_input['id']

    	# add shingles of the current document to its json
    	# write it to a seperate file
    	json_input['shingles'] = shingler(content, preprocess, shingle_size, hash_seed)

		output_file = join(output_path, doc_id)

    	with open(output_file, 'w') as outfile:
    		json.dump(data, outfile)
