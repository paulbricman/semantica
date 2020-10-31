from semantica import Semantica
s = Semantica('./models/GoogleNews-vectors-negative300.bin', word_count=100000)

samples = []

#samples += [s.field("tree")]
#samples += [s.mix("human", "computer")]
#samples += [s.mix("breakfast", "lunch", "dinner")]
#samples += [s.mix("king", s.shift("man", "woman"))]
#samples += [s.mix("burrito", s.shift("Spain", "Italy"))]
#s.mix("society", s.shift("order", "chaos"))
#s.mix("heaven", s.shift("good", "bad")))
#s.mix("hero", s.shift("good", "bad"))
#s.mix("human", "virus")
#s.mix("computer", "virus")
#import itertools
#for element in itertools.product([True, False], [True, False], [True, False], [True, False]):
#    samples += [s.mix("love", s.shift("human", "computer", norm_concepts=element[0], norm_result=element[1]), norm_concepts=element[2], norm_result=element[3])]
#s.mix("humankind", "space")
#samples += [s.span("person", "society")]
#samples += [s.span("house", "city")]
#samples += [s.span("loser", "winner")]
#samples += [s.span("hope", "despair")]
#samples += [s.span("human", "computer")]
#samples += [s.match("king", "queen")]
#samples += [s.match("tree", "forest")]
samples += [s.match("king", "queen")]

for i in range(len(samples)):
    print('Sample', str(i))
    print(*samples[i])
    print()