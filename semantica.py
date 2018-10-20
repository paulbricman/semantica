import gensim
import ast

class RewriteName(ast.NodeTransformer):

    def visit_Name(self, node):
        return ast.copy_location(ast.Subscript(
            value=ast.Name(id='model', ctx=ast.Load()),
            slice=ast.Index(value=ast.Str(s=node.id)),
            ctx=node.ctx
        ), node)

model = gensim.models.KeyedVectors.load_word2vec_format('model.bin', binary=True)

while True:
    equation_input = input()
    tree = ast.parse(equation_input, mode='eval')
    tree = RewriteName().visit(tree)
    ast.fix_missing_locations(tree)
    results = model.most_similar(positive=[eval(compile(tree, filename='<ast>', mode='eval'))], topn=10)
    print('\nTop Nearest Results:')
    for result in results:
        print('-',result[0])
    print('\n\n')
