def read_movie_genre(f):
    dct = {}
    prevmovie=''
    for line in open(f):
        if prevmovie!=line[line.index('|')+3:].strip('\n'):
            movie = line[line.index('|')+3:].strip('\n')
            genre = line[:line.index('|')]
            #print(movie,genre)

        #genre.append(line[:line.index('|')])
        dct[movie] = genre
        prevmovie=movie
        
    return dct
  
def create_genre_dict(d):
  #genre-movie
 ans = {}
 for(movie,genre) in d.items():
     if genre in ans.keys():
         ans[genre].append(movie)
     else:
         ans[genre] = [movie]

 return ans

create_genre_dict(read_movie_genre('genreMovieSample.txt'))
