import math


def tf(word, blob):
    return blob.words.count(word) / len(blob.words)


def n_containing(word, blob_list):
    return sum(1 for blob in blob_list if word in blob.words)


def idf(word, blob_list):
    return math.log(len(blob_list) / (1 + n_containing(word, blob_list)))


def tf_idf(word, blob, blob_list):
    return tf(word, blob) * idf(word, blob_list)
