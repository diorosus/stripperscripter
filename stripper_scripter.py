path = 'test.txt'
try:
    with open(path, 'r') as infile:
        data = infile.read().replace('hxxp', 'http').replace('[.]', '.').replace('[@]', '@')
except OSError as exception:
    print('ERROR: could not read file:')
    print('  %s' % exception)
else:
    with open(path, 'w') as outfile:
        outfile.write(data)