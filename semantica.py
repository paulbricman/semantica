import gensim


class Semantica:
    def __init__(self, model_path, word_count=1000000):
        self.c = gensim.models.KeyedVectors.load_word2vec_format(
            model_path, binary=True, limit=word_count)

    def field(self, concept):
        gensim_results = self.c.most_similar(concept)
        concepts = [e[0] for e in gensim_results]

        return concepts
