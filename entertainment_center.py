# encoding: utf-8
import fresh_tomatoes
import media

# Here are defined the movie to be displayed and their attributes
toy_story = media.Movie('Toy Story', 'Toys are living things who pretend' +
                        ' to be lifeless when humans are present',
                        'https://goo.gl/hk1VY1',
                        'https://www.youtube.com/watch?v=KYz2wyBy3kc')

avengers = media.Movie('Avengers: Infinity War',
                       'Two years after the Avengers, Thanos arrives' +
                       ' on Earth to collect the Infinity Stones',
                       'https://goo.gl/JDjed1',
                       'https://www.youtube.com/watch?v=twXfolLOiHc')

rocky = media.Movie('Rocky', 'Rocky meets with promoter Miles,' +
                    ' presuming Creed is seeking local sparring partners.',
                    'https://goo.gl/31mhrq',
                    'https://www.youtube.com/watch?v=3VUblDwa648')

pulp_fiction = media.Movie('Pulp Fiction', 'Hitmens arrive at an' +
                           ' apartment to retrieve a briefcase' +
                           ' for their boss.',
                           'https://goo.gl/SB2Sbz',
                           'https://www.youtube.com/watch?v=s7EdQ4FqbhY&t=34s')

inglorious_basterds = media.Movie('Inglorious Basterds', 'In 1941, ' +
                                  'SS colonel interrogates French ' +
                                  'dairy farmer.',
                                  'https://goo.gl/9X4s1r',
                                  'https://www.youtube.com/' +
                                  'watch?v=qRYDNWXuip8')

django = media.Movie('Django', 'In 1858 Texas, the Speck brothers' +
                     ' drive a group of black slaves on foot.',
                     'https://goo.gl/KZxsuT',
                     'https://www.youtube.com/watch?v=s8CZKbDzP1E')

# Here is the list of movies that will be used
# by the fresh_tomatoes.py program to build the site
movies = [toy_story, avengers, rocky,
          pulp_fiction, inglorious_basterds, django]

# The fresh_tomatoes program builds the site
fresh_tomatoes.open_movies_page(movies)
