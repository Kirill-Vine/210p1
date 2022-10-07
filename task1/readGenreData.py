def read_movie_genre(f):
    dct = {}
    prevmovie=''
    for line in open(f):
        if prevmovie!=line[line.index('|')+3:].strip('\n'):
            movie = line[line.index('|')+3:].strip('\n|')
            genre = line[:line.index('|')]
        dct[movie] = genre
        prevmovie=movie
    return dct
read_movie_genre('genreMovieSample.txt')
