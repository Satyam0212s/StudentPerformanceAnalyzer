def pass_fail_analysis(df):

    subjects = [
        "math",
        "physics",
        "chemistry",
        "english",
        "computer"
    ]

    df["status"] = df[subjects].apply(
        lambda row:
        "Pass"
        if all(mark >= 40 for mark in row)
        else "Fail",
        axis=1
    )

    passed = (df["status"] == "Pass").sum()
    failed = (df["status"] == "Fail").sum()

    print("\n========== PASS FAIL REPORT ==========\n")

    print(f"Passed Students : {passed}")
    print(f"Failed Students : {failed}")