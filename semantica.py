import gensim
from gensim import matutils

import numpy as np
from numpy import ndarray, float32, array

class Semantica:
    def __init__(self, model_path, word_count=1000000):
        self.c = gensim.models.KeyedVectors.load_word2vec_format(
            model_path, binary=True, limit=word_count)

    def field(self, concept):
        concepts = self.c.most_similar(concept)
        concepts = [e[0] for e in concepts]

        return concepts

    def shift(self, source, target):
        source_vector = -self.c.get_vector(source)
        target_vector = self.c.get_vector(target)

        shift = matutils.unitvec(array([source_vector, target_vector]).mean(axis=0)).astype(float32)

        return shift