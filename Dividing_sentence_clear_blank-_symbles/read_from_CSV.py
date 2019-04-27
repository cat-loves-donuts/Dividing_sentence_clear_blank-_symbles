import csv

#import numpy as np

a = c = x = e = positive = negative = word_test = length = word_size_pos = word_size_neg = 0
def take_part(l):
    ulist = []
    [ulist.append(y) for y in l if y not in ulist]
    return ulist

def have_repit_word(w):
    new_list = []
    [new_list.append(y) for y in w]
    return new_list

with open("sentence in tow emotion.csv") as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]
for i in range(9059):
    b = str(rows[i][0])
    b = have_repit_word(b.split(' '))
    a = a + len(b)

for i in range(9059):
    if rows[i][1] == 'positive':
        d = str(rows[i][0])
        d = have_repit_word(d.split(' '))
        c = c + len(d)
        positive = positive + 1
    else:
        f = str(rows[i][0])
        f = have_repit_word(f.split(' '))
        e = e + len(f)
        negative = negative + 1

for i in range(9059):
    word_sentence = str(rows[i][0])
    word_sentence = word_sentence.replace(',', ' ')
    word_sentence = word_sentence.replace('.', ' ')
    word_sentence = word_sentence.replace('-', ' ')
    word_sentence = word_sentence.replace('_', ' ')
    word_sentence = word_sentence.replace('!', ' ')
    word_sentence = word_sentence.replace('/', ' ')
    word_sentence = word_sentence.replace('|', ' ')
    word_sentence = word_sentence.replace(';', ' ')
    word_sentence = word_sentence.replace(':', ' ')
    word_sentence = word_sentence.replace('""', ' ')
    word_sentence = word_sentence.replace("''", " ")
    word_sentence = word_sentence.replace("'", ' ')
    word_sentence = word_sentence.replace('"', ' ')
    word_sentence = word_sentence.replace('?', ' ')
    word_sentence = word_sentence.replace('`', ' ')
    word_sentence = word_sentence.replace('~', ' ')
    word_test = take_part(word_sentence.split(' '))
    for z in word_test:
        if z == '':
            word_test.remove('')
    x = x + len(word_test)
    print(word_test)
    if rows[i][1] == 'positive':
        word_size_pos = word_size_pos + len(word_test)
    else:
        word_size_neg = word_size_neg + len(word_test)
    length = 0

print("---------------result---------------")
print('The length of all sentences : ',a)
print('over all average sentence length : ', (a/9059))
print('The number of positive sentences : ', positive)
print('The length of positive sentences : ', c)
print('The average positive sentences length', (c/positive))
print('The number of negative sentences : ', negative)
print('The length of negative sentences : ', e)
print('The average negative sentences length', (e/negative))
print('The overall vocabulary size : ', x)
print('The word size of positive sentences : ', word_size_pos)
print('The word size of negative sentences : ', word_size_neg)



'''with open("sentence in tow emotion.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    for i in range(9059):
        if float(rows[i][1]) > 0.6:
            rows[i][1] = 'positive'
        else:
            rows[i][1] = 'negative'
        writer.writerow([rows[i][0],rows[i][1]])'''