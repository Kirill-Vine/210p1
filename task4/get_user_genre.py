def read_movie_genre(f): #1.2
    dct = {}
    prevmovie=''
    for line in open(f):
        if prevmovie!=line[line.index('|')+3:].strip('\n'):
            movie = line[line.index('|')+3:].strip('\n|')
            genre = line[:line.index('|')]
        dct[movie] = genre
        prevmovie=movie
    return dct
def read_user_ratings(f): #4.1
    dct = {}
    for line in open(f):
        if line[line.index('|')+5:].strip('\n') not in dct:
            dct[line[line.index('|')+5:].strip('\n')] = list()
        dct[line[line.index('|')+5:].strip('\n')].append(tuple((line[:line.index('|')],line[line.index('|')+1:line.index('|')+4])))
    return dct 
def get_user_genre(uid,f,e):
    dct = f.get(str(uid))
    lst=list()
    movie=None
    for i in dct:
        lst.append(i[1])
    for i in dct:
        if i[1]==max(lst):
            movie=i[0]
    genre=e.get(str(movie))
    return genre
get_user_genre(43,read_user_ratings("movieRatingSample.txt"), read_movie_genre('genreMovieSample.txt'))
