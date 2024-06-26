 marks_mathematics_premise = 76
marks_science_premise = 65
marks_social_studies_premise = 82
marks_english_premise = 67
marks_biology_premise = 75

marks_mathematics_hypothesis = 76
marks_science_hypothesis = 65
marks_social_studies_hypothesis = 82
marks_english_hypothesis = 67
marks_biology_hypothesis = 75

# the hypothesis mentions the marks obtained by Shekar in various subjects, which are also mentioned in the premise
if marks_mathematics_premise!= marks_mathematics_hypothesis or marks_science_premise!= marks_science_hypothesis or marks_social_studies_premise!= marks_social_studies_hypothesis or marks_english_premise!= marks_english_hypothesis or marks_biology_premise!= marks_biology_hypothesis:
    # check if any of the marks in the hypothesis contradicts the marks mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis marks do not contradict the premise marks, we can infer entailment
    label = "entailment"

print(label)

