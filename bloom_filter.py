# requires bitarray and mmh3
# pip install bitarray
# pip install mmh3

import json
import murmur3

try:
    import mmh3 as mmh3
except ImportError:
    import mmh3_py as mmh3

from os import listdir
from os.path import isfile, join
from bitarray import bitarray

# requires python bitarray
def generate_bloom_filters(input_path, hash_size, number_of_hashes, output_path, write_to_file=True):
	bloom_filter = bitarray(2**hash_size)

	files = [f for f in listdir(input_path) if isfile(join(input_path, f))]

	for infile in files:
    	json_input = json.loads(doc)
    	if 'shingles' not in json_input or 'content' not in json_input or 'published' not in json_input or 'id' not in json_input:
    		continue

    	shingles = json_input['shingles']
    	doc_id = json_input['id']
		# set the bits for corresponding shingle using n hash functions
		for shingle in shingles:
			hashes = generate_bloom_hashes(input, hash_size, number_of_hashes)
			for hash_val in hashes:
				bloom_filter[hash_val] = 1

		output_file = join(output_path, doc_id)
		write_bloom_filter_to_file(bloom_filter, output_file)


def check_exists_in_bloom_filter(bloom_filter, input, hash_size, number_of_hashes):
	input_hashes = generate_bloom_hashes(input, number_of_hashes, hash_size)

	for hash_val in hashes:
		if bloom_filter[hash_val] == 0:
			return False
	return True


def calc_bloom_filter_metrics(bloom_filter, input, hash_size, number_of_hashes):
	
	containment = 0
	similarity = 0

	# todo


	return (containment, similarity)

def find_candidate_pairs()




# we can generate n different hashes only calling the hash function twice as shown here
# Less Hashing, Same Performance: Building a Better Bloom Filter
# a.k.a Kirsch-Mitzenmacher-Optimization 
def generate_bloom_hashes(input, hash_size, number_of_hashes):
	hashes = []

	for hashes in xrange(number_of_hashes):
		# generate two hashes of 4 bytes convert to integer
		hash_val1 = input
		hash_val2 = numpy.uint32(mmh3.hash(hash_val1))

		hashes.append((hash_val1 + hashes * hash_val2) % hash_size)

	return hashes


def write_bloom_filter_to_file(bloom_filter, output_file):
	with open(output_file, 'wb') as outfile:
		bloom_filter.tofile(outfile)


def read_bloom_filter_from_file(input_file):
	bloom_filter = bitarray()
	with open(input_file, 'rb') as infile:
		a.fromfile(infile)



