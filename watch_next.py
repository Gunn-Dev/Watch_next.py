import spacy
from sklearn.metrics.pairwise import cosine_similarity

def load_movies(file_path):
    movies = {}
    with open(file_path, 'r') as file:
        for line in file:
            title, description = line.strip().split(':', 1)
            movies[title.strip()] = description.strip()
    return movies

def find_most_similar_movie(input_description, movies):
    nlp = spacy.load('en_core_web_md')
    input_description_vector = nlp(input_description).vector

    max_similarity = -1
    most_similar_movie = None

    for title, description in movies.items():
        movie_vector = nlp(description).vector
        similarity = cosine_similarity([input_description_vector], [movie_vector])[0][0]

        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_movie = title

    return most_similar_movie

if __name__ == "__main__":
    movies_file_path = "movies.txt"
    movies = load_movies(movies_file_path)

    input_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."

    most_similar_movie = find_most_similar_movie(input_description, movies)
    print("Next movie to watch:", most_similar_movie)
