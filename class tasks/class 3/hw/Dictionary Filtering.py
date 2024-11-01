# Example 9: Dictionary Filtering Based on Conditions

scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 95}
passed_students = {name: score for name, score in scores.items() if score >= 80}

print(passed_students)