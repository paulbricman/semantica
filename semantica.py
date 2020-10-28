import gensim
from gensim import matutils

import numpy as np
from numpy import ndarray, float32, array, dot, mean


class Semantica:
    def __init__(self, model_path, word_count=1000000):
        self.c = gensim.models.KeyedVectors.load_word2vec_format(
            model_path, binary=True, limit=word_count)

    def to_vector(self, concept, norm=True):
        if isinstance(concept, ndarray):
            return concept
        else:
            if norm:
                return matutils.unitvec(self.c.get_vector(concept))
            else:
                return self.c.get_vector(concept)

    def field(self, concepts, norm=True):
        fields = []

        if isinstance(concepts, (str, ndarray)):
            concepts = [concepts]

        for concept in concepts:
            field = self.c.most_similar([self.to_vector(concept, norm=norm)])
            field = [e[0] for e in field]
            fields += [field]

        return fields

    def mix(self, concepts, norm=True):
        concept_vectors = []

        for concept in concepts:
            concept_vectors += [self.to_vector(concept, norm=norm)]

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

    def model(self, model, match_threshold=0.6):
        root = model[0]
        skeleton = [self.shift(root, e) for e in model[1:]]
        matches = []

        for i in range(len(self.c.vectors)):
            match_score = []
            new_leaf_concepts = []

            new_root_vector = self.c.vectors[i]
            new_leaf_vectors = [self.mix([new_root_vector, skeleton[j]]) for j in range(len(skeleton))]

            new_root_concept = self.c.similar_by_vector(new_root_vector)[0][0]
            new_leaf_concepts = []

            for new_leaf_vector in new_leaf_vectors:
                new_leaf_concept = [e[0] for e in self.c.similar_by_vector(new_leaf_vector) if e[0] not in [new_root_concept, *new_leaf_concepts]][0]
                new_leaf_concepts += [new_leaf_concept]

            for i in range(len(new_leaf_vectors)):
                match_score += [dot(self.shift(new_root_concept, new_leaf_concepts[i]), skeleton[i])]

            for i in range(len(new_leaf_vectors)):
                match_score += [dot(matutils.unitvec(new_leaf_vectors[i]), matutils.unitvec(self.to_vector(new_leaf_concepts[i])))]

            #if "man" in [e[0] for e in self.c.similar_by_vector(new_root)]:
            #    print('---', [e for e in [self.c.similar_by_vector(e) for e in [new_root] + new_leafs]], sep='\n')

            match_score = mean(match_score)

            if match_score > match_threshold:
                match = [new_root_concept, *new_leaf_concepts]
                #matches += [new_root, *new_leafs]
                print('---', *self.field(match), sep='\n')
                print(match_score)