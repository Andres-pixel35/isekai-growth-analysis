import pandas as pd

path = "../data/Animes.csv"


# compouned annual growth rate
def cagr(start_value, end_value, years):
    return (end_value / start_value) ** (1 / years) - 1

# create data frame df and isekai_df and return both of them
def cidf():
    df = pd.read_csv(path, usecols=["Title", "Release", "Theme"])

    df = df.dropna(subset=["Theme"])

    df["Release"] = pd.to_datetime(df["Release"], format="mixed")
    df = df[df["Release"].dt.year > 1999]

    isekai_df = df[df["Theme"].str.contains("isekai", case=False, na=False)]

    return df, isekai_df
