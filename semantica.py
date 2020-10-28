import gensim
from gensim import matutils

import numpy as np
from numpy import ndarray, float32, array


class Semantica:
    def __init__(self, model_path, word_count=1000000):
        self.c = gensim.models.KeyedVectors.load_word2vec_format(
            model_path, binary=True, limit=word_count)

    def to_vector(self, concept, norm=False):
        if isinstance(concept, ndarray):
            return concept
        else:
            if norm:
                return matutils.unitvec(self.c.get_vector(concept))
            else:
                return self.c.get_vector(concept)

    def field(self, concept):
        field = self.c.most_similar([self.to_vector(concept, norm=True)])
        field = [e[0] for e in field]

        return field

    def mix(self, concepts):
        concept_vectors = []

        for concept in concepts:
            concept_vectors += [self.to_vector(concept, norm=True)]

        mix = matutils.unitvec(
            array(concept_vectors).mean(axis=0)).astype(float32)

        return mix

    def shift(self, source, target):
        source_vector = -self.to_vector(source, norm=True)
        target_vector = self.to_vector(target, norm=True)

        shift = matutils.unitvec(
            array([source_vector, target_vector]).mean(axis=0)).astype(float32)

        return shift
