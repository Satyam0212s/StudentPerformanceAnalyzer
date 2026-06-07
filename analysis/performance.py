def assign_performance_category(percentage):

    if percentage >= 90:
        return "Excellent"

    elif percentage >= 75:
        return "Good"

    elif percentage >= 60:
        return "Average"

    else:
        return "Needs Improvement"