marks_maths_premise = 76
marks_maths_hypothesis = 46

marks_science_premise = 65
marks_science_hypothesis = 65

marks_social_studies_premise = 82
marks_social_studies_hypothesis = 82

marks_english_premise = 67
marks_english_hypothesis = 67

marks_biology_premise = 75
marks_biology_hypothesis = 75

# the hypothesis refers to the marks scored by Shekar in each subject, as mentioned in the premise
if marks_maths_hypothesis < marks_maths_premise:
    label = "entailment"
elif marks_science_hypothesis!= marks_science_premise or marks_social_studies_hypothesis!= marks_social_studies_premise or marks_english_hypothesis!= marks_english_premise or marks_biology_hypothesis!= marks_biology_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
