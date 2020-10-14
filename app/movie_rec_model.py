# Importing necessary modules
import pickle
import re
from fuzzywuzzy import fuzz

def print_recommendations(knn_output):
    '''Function to print output from movie list'''    
    
    with open('movie_list.pkl', 'rb') as file:
        movie_list = pickle.load(file)
    
    distances, indices = knn_output
    m_selection = []
    
    for i,res in enumerate(zip(distances.flatten(), indices.flatten())):
        distance, index = res
        name = movie_list.iloc[index]['title']
        if i == 0:
            or_movie = f'Users who liked {name} also like:'
        else:
            m_selection.append(name)
    
    return or_movie, m_selection
            

            
def movieid_vec(movie_id):
    '''Creates vector array for the KNN model'''  
    with open('movie_features.pkl', 'rb') as file:
        movie_features = pickle.load(file)
    
    return movie_features.loc[movie_id].values.reshape(1, -1)


def get_movieid(query):
    '''Filters queries through movie titles'''    
    
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

def recommend_movies(query, n=5):
    '''Final function which uses actual KNN model on sparse matrix'''    
    with open('model_knn.pkl', 'rb') as file:
        model_knn = pickle.load(file)
    
    movie_id = get_movieid(query)
    if not movie_id:
        return
    
    movie_vec = movieid_vec(movie_id)
    
    n_recs = n + 1
    recs = model_knn.kneighbors(movie_vec, n_neighbors=n_recs)
    
    return print_recommendations(recs)
    

if __name__ == '__main__':
     print(recommend_movies('walley'))   
    
    
    
    
    
    