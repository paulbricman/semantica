from semantica import Semantica

s = Semantica()

print('Field samples')
print(s.field('car'))
print(s.field('galaxy'))
print(s.field('bed'))

print('\nMix samples')
print(s.mix('people', 'chaos'))
print(s.mix('computer', 'virus'))
print(s.mix('brain', 'science'))

print('\nSpan samples')
print(s.span('pond', 'ocean'))
print(s.span('city', 'house'))
print(s.span('kindergarten', 'university'))

print('\nShift samples')
print(s.mix('cell', s.shift('biology', 'physics')))
print(s.mix('saxophone', s.shift('jazz', 'rock')))
print(s.mix('burrito', s.shift('Spain', 'Italy')))

print('\nMatch samples')
print(s.match('people', 'society'))
print(s.match('king', 'queen', target='acting'))
print(s.match('physics', 'Einstein', target='science'))