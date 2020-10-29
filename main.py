from semantica import Semantica

s = Semantica('./models/GoogleNews-vectors-negative300.bin', word_count=100000)

samples = []

samples += [s.field("tree")]
samples += [s.mix("breakfast", "lunch")]
samples += [s.mix("king", shift=["man", "woman"])]
samples += [s.mix("burrito", shift=["Spain", "Italy"])]

for i in range(len(samples)):
    print('Sample', str(i))
    print(*samples[i])
    print()