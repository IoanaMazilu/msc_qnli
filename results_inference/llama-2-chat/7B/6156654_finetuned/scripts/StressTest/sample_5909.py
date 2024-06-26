marks_math = 76
marks_science = 65
marks_social_studies = 82
marks_english = 67
marks_biology = 75

# the hypothesis refers to the marks Shekar scored in each subject, which are also mentioned in the premise
if marks_math <= marks_math or marks_science <= marks_science or marks_social_studies <= marks_social_studies or marks_english <= marks_english or marks_biology <= marks_biology:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
