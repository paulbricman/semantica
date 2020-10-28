from semantica import Semantica

s = Semantica('./models/GoogleNews-vectors-negative300.bin', word_count=100000)

print(s.field([s.mix(["king", s.shift("man", "woman")]), "tree"]))