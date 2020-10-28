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

    def field(self, concepts):
        fields = []

        if isinstance(concepts, (str, ndarray)):
            concepts = [concepts]

        for concept in concepts:
            field = self.c.most_similar([self.to_vector(concept, norm=True)])
            field = [e[0] for e in field]
            fields += [field]

        return fields

    def mix(self, concepts):
        concept_vectors = []

        for concept in concepts:
            concept_vectors += [self.to_vector(concept, norm=True)]

        mix = matutils.unitvec(
            array(concept_vectors).mean(axis=0)).astype(float32)

        return mix

    def shift(self, source, target, norm=True):
        source_vector = -self.to_vector(source, norm=norm)
        target_vector = self.to_vector(target, norm=norm)

        shift = matutils.unitvec(
            array([source_vector, target_vector]).mean(axis=0)).astype(float32)

        return shift

    def span(self, start, end, steps=5):
        step_vectors = []
        shift = self.shift(start, end)

        for step in range(1, steps + 1):
            step_vector = self.mix([start, shift * (1 / steps) * step])
            step_vectors += [step_vector]

        return step_vectors

