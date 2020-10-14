from flask import Flask, render_template, request
from movie_rec_model import recommend_movies 

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])

def run_recommender():
    
    if request.method == 'POST':
        query = request.form['query']
        
        if recommend_movies(query, n=5) is None:
            return render_template('index.html')
        else:
            info, recommendation = recommend_movies(query, n=5)
        
        return render_template('index.html', output=recommendation, info=info)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)
#app.run(host='0.0.0.0', port=8000)