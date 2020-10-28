import gensim

class Semantica:
    def __init__(self, model_path, word_count=1000000):
        self.w = gensim.models.KeyedVectors.load_word2vec_format(model_path, binary=True, limit=word_count)