import pandas as pd

def calculate_statistics(df):

    subjects = [
        "math",
        "physics",
        "chemistry",
        "english",
        "computer"
    ]

    print("\n========== SUBJECT STATISTICS ==========\n")

    for subject in subjects:

        mean = df[subject].mean()
        median = df[subject].median()
        highest = df[subject].max()
        lowest = df[subject].min()

        print(f"{subject.upper()}")

        print(f"Mean Score   : {mean:.2f}")
        print(f"Median Score : {median}")
        print(f"Highest Score: {highest}")
        print(f"Lowest Score : {lowest}")

        print("-" * 35)