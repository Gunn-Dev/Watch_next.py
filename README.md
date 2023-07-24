# Movie Recommender

This is a simple movie recommender system that suggests the most similar movie based on an input description. It uses Natural Language Processing (NLP) techniques to compute the similarity between movie descriptions.

## Requirements

- Python 3.8 or higher
- `spaCy` and `scikit-learn` Python libraries (see `requirements.txt`)

## Getting Started

1. Clone the repository:

git clone https://github.com/<your-github-username>/movie-recommender.git


2. Install the required dependencies:

pip install -r requirements.txt

3. Run the movie recommender:

python watch_next.py

The program will prompt you to enter a movie description, and it will recommend the most similar movie from the list of available movies in `movies.txt`.

## How it Works

The recommender system uses the `spaCy` library for Natural Language Processing (NLP) and cosine similarity to measure the similarity between movie descriptions. The `watch_next.py` script loads the movie descriptions from the `movies.txt` file, tokenizes and vectorizes the input description and each movie description using `spaCy`, and then computes the cosine similarity between the vectors. The movie with the highest similarity score is recommended as the next movie to watch.

## Input Description Format

The input description should be a brief description of the movie in plain English text. For example:

Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator.

## Example Output

Next movie to watch: Movie F


## Data Source

The movie descriptions are provided in the `movies.txt` file.

## Acknowledgments

This project is a simple demonstration of using NLP techniques for similarity matching and is for educational purposes only.

Feel free to modify, improve, and expand the project as you like!

