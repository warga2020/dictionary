# f = open('sample.txt', 'r')

import text_processor.text_processor as tp

f = open('sample.txt', 'r')
lines = ''.join(f.readlines())

tokens = tp.extract_tokens(lines)
tp.clean_tokens(tokens)
tp.cutoff_suffixes(tokens)
tp.delete_invalid_tokens(tokens)

tokens = tp.remove_duplicates(tokens)

tokens.sort()
for s in tokens:
    print(s)
