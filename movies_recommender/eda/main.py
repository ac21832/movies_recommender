import pandas as pd
from pathlib import Path
from matplotlib import pyplot as plt

def load_dataset(dataset_path: Path) -> pd.DataFrame:
    df = pd.read_csv(dataset_path, low_memory=False)
    return df

def preview_dataset(df: pd.DataFrame) -> None:
    with pd.option_context('display.max_rows', 5, 'display.max_columns', None): 
        print(df.head())
    print(df.describe())


def analyze_adult(df: pd.DataFrame) -> None:
    encoded_adult = df["adult"].apply(lambda x: 1 if x == "True" else 0)
    hist = encoded_adult.hist()
    hist.plot()
    plt.show()

if __name__ == "__main__":
    df = load_dataset(Path("data/movies_metadata.csv"))
    preview_dataset(df)
    analyze_adult(df)