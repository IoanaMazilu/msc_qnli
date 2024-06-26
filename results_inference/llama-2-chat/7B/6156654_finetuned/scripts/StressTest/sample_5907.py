marks_mathematics = 76
marks_science = 65
marks_social_studies = 82
marks_english = 67
marks_biology = 75

marks_greater_than = 46

# the hypothesis refers to the marks in each subject, which are also mentioned in the premise
if marks_mathematics >= marks_greater_than:
    label = "entailment"
elif marks_science >= marks_greater_than:
    label = "entailment"
elif marks_social_studies >= marks_greater_than:
    label = "entailment"
elif marks_english >= marks_greater_than:
    label = "entailment"
elif marks_biology >= marks_greater_than:
    label = "entailment"
else:
    label = "contradiction"

print(label)
