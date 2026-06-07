from analysis.performance import assign_performance_category


def generate_rankings(df):

    subjects = [
        "math",
        "physics",
        "chemistry",
        "english",
        "computer"
    ]

    df["total"] = df[subjects].sum(axis=1)

    df["percentage"] = round(
        df["total"] / 5,
        2
    )

    df["rank"] = (
        df["total"]
        .rank(
            ascending=False,
            method="dense"
        )
        .astype(int)
    )

    df["category"] = df["percentage"].apply(
        assign_performance_category
    )

    ranked_df = df.sort_values(
        by="rank"
    )

    return ranked_df