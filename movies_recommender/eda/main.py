from collections import Counter
import pandas as pd
from pathlib import Path
from matplotlib import pyplot as plt
import numpy as np


def is_float(raw_number: str) -> bool:
    try:
        _ = float(raw_number)

    except:
        return False

    return True


def load_dataset(dataset_path: Path) -> pd.DataFrame:
    df = pd.read_csv(dataset_path, low_memory=False)
    print(f"Original size: {df.size}")
    df = df[df["budget"].apply(lambda x: is_float(x))]
    print(f"New size: {df.size}")
    df["budget"] = df["budget"].apply(lambda x: float(x))
    df["genres"] = (
        df["genres"]
        .apply(lambda raw_genres: eval(raw_genres))
        .apply(lambda genres: set([g["name"] for g in genres]))
    )
    return df


def preview_dataset(df: pd.DataFrame) -> None:
    with pd.option_context("display.max_rows", 5, "display.max_columns", None):
        print(df.head())
    print(df.describe())


def analyze_adult(df: pd.DataFrame) -> None:
    encoded_adult = df["adult"].apply(lambda x: 1 if x == "True" else 0)
    hist = encoded_adult.hist()
    hist.plot()
    plt.show()


def analyze_budget(df: pd.DataFrame) -> None:
    hist = df["budget"].hist()
    hist.plot()
    plt.show()
    with pd.option_context("display.float_format", "{:.2f}".format):
        print(df["budget"].describe())


def analyze_rating(df: pd.DataFrame) -> None:
    hist = df["vote_average"].hist()
    hist.plot()
    plt.show()


def analyze_genres(df: pd.DataFrame) -> None:
    genres_lists = list(df["genres"])
    flatten = [genre for genres_list in genres_lists for genre in genres_list]
    genres_count = Counter(flatten)
    print(genres_count)


if __name__ == "__main__":
    df = load_dataset(Path("data/movies_metadata.csv"))
    preview_dataset(df)
    # analyze_adult(df)
    # analyze_budget(df)
    # analyze_rating(df)
    analyze_genres(df)
