marks_math = 76
marks_science = 65
marks_social_studies = 82
marks_english = 67
marks_biology = 75

marks_more_than = 46
marks_math_more_than = marks_math - marks_more_than
marks_science_more_than = marks_science - marks_more_than
marks_social_studies_more_than = marks_social_studies - marks_more_than
marks_english_more_than = marks_english - marks_more_than
marks_biology_more_than = marks_biology - marks_more_than

# the hypothesis refers to the marks scored by Shekar in each subject
if marks_math <= marks_math_more_than:
    label = "contradiction"
elif marks_science <= marks_science_more_than:
    label = "contradiction"
elif marks_social_studies <= marks_social_studies_more_than:
    label = "contradiction"
elif marks_english <= marks_english_more_than:
    label = "contradiction"
elif marks_biology <= marks_biology_more_than:
    label = "contradiction"
else:
    label = "neutral"

print(label)
