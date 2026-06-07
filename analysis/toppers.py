def subject_toppers(df):

    subjects = [
        "math",
        "physics",
        "chemistry",
        "english",
        "computer"
    ]

    print("\n========== SUBJECT TOPPERS ==========\n")

    for subject in subjects:

        max_marks = df[subject].max()

        topper = df[df[subject] == max_marks]

        print(
            f"{subject.upper()} : "
            f"{topper.iloc[0]['name']} "
            f"({max_marks})"
        )