from pathlib import Path
from typing import Literal
from movies_recommender.eda.main import load_dataset
from movies_recommender.models import Criteria
import pandas as pd

from movies_recommender.thresholds import (
    IS_AMATEUR_MOVIE,
    VOTE_AVERAGE_LOW,
    VOTE_AVERAGE_MEDIUM,
)


def rank_movie(movie: pd.Series, criteria: Criteria) -> list[int]:
    number_of_matched_genres = len(
        movie.genres.intersection(set(criteria.target_genres))
    )
    is_movie_amateur = movie.budget < IS_AMATEUR_MOVIE
    is_amateur_matching = int(is_movie_amateur == criteria.is_amateur)
    movie_rating_category = determine_rating_category(movie.vote_average)
    is_rating_category_matching = int(
        movie_rating_category == criteria.target_rating_category
    )

    return [is_amateur_matching, is_rating_category_matching, number_of_matched_genres]


def determine_rating_category(average_rating: int) -> Literal["LOW", "MEDIUM", "HIGH"]:
    if average_rating > VOTE_AVERAGE_LOW[0] and average_rating < VOTE_AVERAGE_LOW[1]:
        return "LOW"
    elif (
        average_rating > VOTE_AVERAGE_MEDIUM[0]
        and average_rating < VOTE_AVERAGE_MEDIUM[1]
    ):
        return "MEDIUM"
    return "HIGH"


if __name__ == "__main__":
    is_amateur = True
    rating = "HIGH"
    genres = ["Action"]

    criteria = Criteria(
        is_amateur=is_amateur, target_rating_category=rating, target_genres=genres
    )
    all_movies = load_dataset(Path("data/movies_metadata.csv"))

    titles_with_scores = []
    for idx, movie in all_movies.iterrows():
        score = rank_movie(movie, criteria)
        titles_with_scores.append([movie.title, score])

    sorted_movies = sorted(titles_with_scores, key=lambda x: x[1], reverse=True)
    top_titles = [m for m in sorted_movies[:5]]
    print(top_titles)
