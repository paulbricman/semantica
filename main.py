from semantica import Semantica

s = Semantica('./models/GoogleNews-vectors-negative300.bin', word_count=10000)

print(s.field("tree"))