# ud036_StarterCode
Source code for a Movie Trailer website.
### Final project - Web page with videos
### Installation:
* You need to install  <a target="_blank" rel="noreferrer" href="https://www.python.org/">Python 3.6</a> and copy all files from ud036_StarterCode to the same folder on your computer. Then, run enterteinment_center.py. 
### Development
* This project is basically divided into three modules in Python: media.py, enterteinment_center.py and fresh_tomatoes_py.
### The media.py program contains:
* A data structure (that is, a Python Class named Movie) that will store movie assets, including the title, description, cover URL, and a YouTube link to the movie trailer.
* A method called show_trailer to display the movie trailer
### The entertainment_center.py program:
* Creates multiple instances of that Movie class to represent the movies and groups all instances into a list. In this program there is a constructor for the Movie class that will create the instances of the movies.
* In entertainment_center.py, a list of these movie objects is defined by calling the `media.Movie ()` constructor to instantiate movie objects. These objects can be stored in a list data structure. To generate the site that displays the movie trailers, a source code repository containing a Python module called `fresh_tomatoes.py` was provided by Udacity.
### The fresh_tomatoes.py program:
* The module fresh_tomatoes.py has a function called `open_movies_page ()`, which takes an argument, which is a list of movies, and creates an HTML file that will display all the movies in the list.
* This list of movies is what the `open_movies_page ()` function needs as input to build the HTML file, to display the site.
### Copyright
* The programs have educational purposes and all the images and videos presented here are copyright.
