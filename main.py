from semantica import Semantica

s = Semantica('./models/GoogleNews-vectors-negative300.bin', word_count=1000000)

print(*s.field([s.mix(["king", s.shift("man", "woman")]), "tree"]), sep='\n')
print(*s.field(s.span("male", "female")), sep='\n')