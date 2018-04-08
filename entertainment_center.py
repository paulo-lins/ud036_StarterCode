# encoding: utf-8
import fresh_tomatoes
import media


toy_story = media.Movie('Toy Story', 'Woody, um cowboy de pano e o brinquedo',
                        'https://vignette.wikia.nocookie.net/disney/images/8/80/Toy_Story_-_Poster.jpg/revision/latest?cb=20150108180742',
                        'https://www.youtube.com/watch?v=KYz2wyBy3kc')

avatar = media.Movie('Avatar', 'ma das luas dphae um precioso minério chamado Unobtainium.',
                     'https://observatoriodocinema.bol.uol.com.br/wp-content/uploads/2017/01/avatar-poster.jpg',
                     'https://www.youtube.com/watch?v=KYk0zVOAOgQ')

rocky = media.Movie('Rocky', 'Para se preparar para a luta, Rocky treina com o ex-lutador Mickey Goldmill, enquanto o seu melhor amigo, Paulie, um trabalhador de frigorífico, o deixa praticar socos nas carcaças penduradas no freezer.',
                    'http://www.cafecomfilme.com.br/media/k2/items/cache/aa42b77ec5ce90a2a470158da526f7c4_XL.jpg',
                    'https://www.youtube.com/watch?v=3VUblDwa648')

pulp_fiction = media.Movie('Pulp Fiction', 'Dirigido de uma forma altamente estilizada, Pulp Fiction narra três histórias diferentes, todavia entrelaçadas, sobre dois assassinos profissionais, o gângster que os chefia e sua esposa, um pugilista pago para perder uma luta e um casal assaltando um restaurante, em Los Angeles na década de 1990.',
                           'https://upload.wikimedia.org/wikipedia/pt/8/82/Pulp_Fiction_cover.jpg',
                           'https://www.youtube.com/watch?v=s7EdQ4FqbhY&t=34s')

inglorious_bastards = media.Movie('Inglorious Bastards', 'Em 1941, o Coronel da SS Hans Landa chega a uma fazenda de leite na França ocupada pelos nazis com o intuito de interrogar Perrier LaPadite sobre rumores de que ele estaria a esconder uma família judaica chamada Dreyfus. Landa faz com que fazendeiro confesse que ele os esconde debaixo da casa. Landa ordena que os soldados da SS entrem na residência e disparem sobre o assoalho do chão. A família é toda morta, com exceção da adolescente Shosanna, que Landa deixa escapar.',
                                  'https://ia.media-imdb.com/images/M/MV5BOTJiNDEzOWYtMTVjOC00ZjlmLWE0NGMtZmE1OWVmZDQ2OWJhXkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_SY1000_SX675_AL_.jpg',
                                  'https://www.youtube.com/watch?v=qRYDNWXuip8')

django = media.Movie ('Django','Situado na era antes da guerra do Deep South e Velho Oeste, o filme acompanha um escravo liberto (Foxx), que caminha por todo os Estados Unidos com um caçador de recompensas (Waltz) em uma missão para resgatar sua esposa (Washington) de um fazendeiro cruel (DiCaprio).',
                      'https://vignette.wikia.nocookie.net/filmguide/images/b/bb/Django-unchained-final-american-movie-poster.jpg/revision/latest?cb=20150109055254'
                      '',
                      'https://www.youtube.com/watch?v=s8CZKbDzP1E')

movies = [toy_story, avatar, rocky, pulp_fiction, inglorious_bastards, django]

fresh_tomatoes.open_movies_page(movies)

