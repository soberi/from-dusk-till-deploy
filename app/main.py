from flask import Flask, render_template, request
from movie_rec_model import recommend_movies
import os

app = Flask(__name__)
port = int(os.environ.get('PORT', 8000))

@app.route('/', methods=['POST','GET'])

def run_recommender():
    
    if request.method == 'POST':
        query = request.form['query']
        
        if recommend_movies(query, n=5) is None:
            error = 'Oops, seems like we don\'t have that one, try another.'
            return render_template('index.html', error=error)
        else:
            # info = movie input by user, recommendation = list of 5 output
            info, recommendation = recommend_movies(query, n=5)
        
        return render_template('index.html', output=recommendation, info=info)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)