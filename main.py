from semantica import Semantica
s = Semantica()

samples = []

samples += [s.field("tree")]
#samples += [s.mix("human", "computer")]
#samples += [s.mix("breakfast", "lunch", "dinner")]
#samples += [s.mix("king", s.shift("man", "woman"))]
#samples += [s.mix("burrito", s.shift("Spain", "Italy"))]
#s.mix("society", s.shift("order", "chaos"))
#s.mix("heaven", s.shift("good", "bad")))
#s.mix("hero", s.shift("good", "bad"))
#s.mix("people", s.shift("society", "brain"))
#s.mix("rocks", "science")
#s.mix("cell", s.shift("biology", "physics"))
#s.mix("skirt", s.shift("she", "he"))
#s.mix("arm", s.shift("elbow", "knee"))
#s.mix("shark", s.shift("sea", "mountain"))
#s.mix("microscope", s.shift("biology", "astronomy"))
#s.mix("Germany", s.shift("Hitler", "Mussolini"))
#s.mix("Christmas", s.shift("Christian", "Jew"))
#s.mix("sea", s.shift("fish", "bird"))
#s.mix("bed", s.shift("bedroom", "bathroom"))
#s.mix("saxophone", s.shift("jazz", "rock"))
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
#s.span("kindergarten", "university")
#s.span("pond", "ocean")
#samples += [s.match("king", "queen")]
#samples += [s.match("tree", "forest")]
#s.match("biology", "cells", target="science")
#s.match("water", "bottle", target="food")
#s.match("physics", "Einstein", target="science")
#s.match("physics", "physicist", target="science")
#s.match("physics", "Einstein", target="arts")
#samples += [s.unmix("two")]
#samples += [s.mix("two", s.shift("one", "two"))]
#samples += [s.mix("one", "three")]

for i in range(len(samples)):
    print('Sample', str(i))
    print(*samples[i])
    print()