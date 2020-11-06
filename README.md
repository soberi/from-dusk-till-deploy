# from-dusk-till-deploy
*A movie recommender based on user ratings, try it out [here](https://from-dusk-till-deploy.herokuapp.com/).*

Tired of the same-ol' same-ol' for the 100th time? Fed up with movie recommenders that just give you second-rate versions of the movie you like? (Finding Nemo is a classic, Shark Tale is a haunting fish nightmare). Well, I've got a recommender for you, instead of similar movies, it compares what users liked. So don't be surprised if Toy Story gives you Jurassic Park, give it a watch and you'll probably love it.


## Why?
The aim of from-dusk-till-deploy was to start out with a dataset and end up with an app, hence the "deploy". While I'm more familiar with the analytics of data, I wanted some practice with backend and allowing users to actually make use of an ML Model (though they probably don't know it).  


## How?
Using data from [MovieLens](https://grouplens.org/datasets/movielens/) and a KNN model, I created an app that takes user input and outputs 5 recommendations. It also handles typos thanks to the python module fuzzywuzzy. You can find a complete overview of the model in my [KNN_movie_recommender notebook](https://github.com/soberi/from-dusk-till-deploy/blob/main/notebooks_analyics/KNN_movie_recommender.ipynb).

I used Flask, Heroku and Gunicorn to get this thing on the world wide web.

The KNN recommender is based on a lecture from my former Data Analytics teacher, so I can't take full credit for that... but I will 100% take credit for winning the battle against Gunicorn and sub-optimal directory paths.
