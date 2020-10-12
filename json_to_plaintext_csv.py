
from __future__ import unicode_literals

import sys
import io
import json

prefix = sys.argv[1]
target = sys.argv[2]

infile = prefix #+ '.json'

data = json.load(open(infile))

#src = io.open(prefix + '.de', 'w', encoding='UTF-8')
target = io.open(prefix + '_' + target, 'w', encoding='UTF-8')
target.write('Error_type' + ',' + 'Incorrect_sentence' + ','+ 'Target_reference_sentence' )

for sentence in data:
    #src.write(sentence['source'] + '\n')
    for error in sentence['errors']:
        #src.write(sentence['source'] + '\n')
        target.write(error['type'] + ',')
        target.write(error['contrastive'] + ',')

    target.write(sentence['reference'] + '\n')

    
