# Movie Recommender System

## Overview

The **Movie Recommender System** is a web-based project that assists users in finding similar movies to the ones they've already watched and enjoyed. This system utilizes machine learning techniques, specifically the **CountVectorizer** model and **cosine similarity** as a distance matrix, to suggest a list of similar movies based on user input.

## Features

- Recommends similar movies based on user input.
- Uses **CountVectorizer** to convert movie titles into numerical vectors.
- Calculates **cosine similarity** to determine the similarity between movies.
- User-friendly web interface built using **Streamlit**.

## How it Works

1. The user selects a movie title from a list of 5000 movies.
2. Upon clicking the "Find Similar Movies" button, the system processes the selected movie.
3. The **CountVectorizer** model transforms the movie titles into numerical vectors.
4. The system calculates the **cosine similarity** between the selected movie and all other movies.
5. The top 5 movies with the highest cosine similarity are displayed as recommendations to the user.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/movie-recommender-system.git
   cd movie-recommender-system

2. Install the required packages using pip:
   ```bash
   pip install -r requirements.txt
3. Run the Streamlit app:
   ```bash
   streamlit run app.py

4. Access the app by visiting http://localhost:8501 in your web browser.

## Usage

1. Open the web application using the link provided after running the app.
2. Choose a movie from the dropdown list.
3. Click the "Find Similar Movies" button.
4. The recommended movies will be displayed below.


## Acknowledgments

- The movie data used for this project was obtained from [source-link](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).
- Special thanks to the **Streamlit** team for providing an intuitive platform for creating interactive web applications.

#### Please find the Screenshots from the WebApp

![Screenshot 2023-08-30 221714](https://github.com/testgithubtiwari/MovieRecommender/assets/111584498/64a18ce8-ceb1-4a6f-802c-7e2c92b88154)

![Screenshot 2023-08-30 221728](https://github.com/testgithubtiwari/MovieRecommender/assets/111584498/26970626-caf6-45f3-8be4-d37eb7fc43d9)



   

