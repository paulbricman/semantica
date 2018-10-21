import gensim
import ast
import random

words = []

class RewriteName(ast.NodeTransformer):

    def visit_Name(self, node):
        words.append(node.id)
        return ast.copy_location(ast.Subscript(
            value=ast.Name(id='model', ctx=ast.Load()),
            slice=ast.Index(value=ast.Str(s=node.id)),
            ctx=node.ctx
        ), node)

model = gensim.models.KeyedVectors.load_word2vec_format('model.bin', binary=True)
print('[*] Model loaded')

while True:
    equation_input = input()

    tree = ast.parse(equation_input, mode='eval')
    tree = RewriteName().visit(tree)
    ast.fix_missing_locations(tree)

    try:
        results = model.most_similar(positive=[eval(compile(tree, filename='<ast>', mode='eval'))], topn=15)
    except KeyError:
        print('Unrecognized word')
    else:
        additional_words = [word+'s' for word in words]+[word.capitalize() for word in words]+[word.capitalize()+'s' for word in words]
        words.extend(additional_words)

        results = [item[0] for item in results if item[0] not in words][:5]
        #random.shuffle(results)
        print(results)

        words.clear()
        additional_words.clear()
