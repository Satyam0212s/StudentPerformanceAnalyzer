import matplotlib.pyplot as plt


def subject_average_chart(df):

    subjects = [
        "math",
        "physics",
        "chemistry",
        "english",
        "computer"
    ]

    averages = [df[subject].mean() for subject in subjects]

    plt.figure(figsize=(8, 5))

    plt.bar(subjects, averages)

    plt.title("Subject Average Scores")
    plt.xlabel("Subjects")
    plt.ylabel("Average Marks")

    plt.tight_layout()

    plt.savefig(
        "output/subject_average_chart.png"
    )

    plt.show()