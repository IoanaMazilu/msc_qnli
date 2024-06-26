marks_maths = 76
marks_science = 65
marks_social_studies = 82
marks_english = 67
marks_biology = 75

# the hypothesis mentions the same marks for each subject as the premise
if marks_maths!= 75 or marks_science!= 65 or marks_social_studies!= 82 or marks_english!= 67 or marks_biology!= 75:
    # check if any of the marks in the hypothesis contradicts the marks in the premise
    label = "contradiction"
else:
    # if the marks in the hypothesis match the marks in the premise, we can infer entailment
    label = "entailment"

print(label)
