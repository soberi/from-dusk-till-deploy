# Importing necessary modules
import pickle
import re
from fuzzywuzzy import fuzz

# Function to print output from movie list
def print_recommendations(knn_output):
    
    with open('movie_list.pkl', 'rb') as file:
        movie_list = pickle.load(file)
    
    distances, indices = knn_output
    
    for i,res in enumerate(zip(distances.flatten(), indices.flatten())):
        distance, index = res
        name = movie_list.iloc[index]['title']
        if i == 0:
            print(f'Users who liked {name} also like:')
            print('----------------------------------------------\n')
        else:
            print(f'{i}: {name}')
            

            
# Creates vector array for the KNN model
def movieid_vec(movie_id):
    
    with open('movie_features.pkl', 'rb') as file:
        movie_features = pickle.load(file)
    
    return movie_features.loc[movie_id].values.reshape(1, -1)


# Filters queries through movie titles
def get_movieid(query):
    
    with open('movie_map.pkl', 'rb') as file:
        movie_map = pickle.load(file)
    
    matches = []
    
    for title, movie_id in movie_map.items():
        
        # removing the year
        year_pattern = r'(.*)\s\(\d{4}\)$'
        extr_title, = re.findall(year_pattern, title)
        
        # get fuzz ration and remove CAsE-sEnsITiVity
        ratio = fuzz.ratio(extr_title.lower(), query)
        
        # ration must be more than 60 in order to match
        if ratio > 60:
            matches.append((extr_title, movie_id, ratio))
    
    if not matches:
        print('Oops, we couldn\'t find what you were looking for.')
        return
    
    # sorts the list of matches, with the highest ratio on top
    return sorted(matches, key=lambda x: x[2], reverse=True)[0][1]

# Final function which uses actual KNN model on sparse matrix
def recommend_movies(query, n=5):
    
    with open('model_knn.pkl', 'rb') as file:
        model_knn = pickle.load(file)
    
    movie_id = get_movieid(query)
    if not movie_id:
        return
    
    movie_vec = movieid_vec(movie_id)
    
    n_recs = n + 1
    recs = model_knn.kneighbors(movie_vec, n_neighbors=n_recs)
    
    print_recommendations(recs)
    

if __name__ == '__main__':
     print(recommend_movies('walley'))   
    
    
    
    
    
    