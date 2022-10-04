def read_user_ratings(f):
    dct = {}
    for line in open(f):
        if line[line.index('|')+5:].strip('\n') not in dct:
            dct[line[line.index('|')+5:].strip('\n')] = list()
        dct[line[line.index('|')+5:].strip('\n')].append(tuple((line[:line.index('|')],line[line.index('|')+1:line.index('|')+4])))
    return dct 
read_user_ratings("movieRatingSample.txt")
