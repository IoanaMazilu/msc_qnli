# Premise: Shekar scored more than 46, 65, 82, 67 and 85 marks in Mathematics, Science, Social studies, English and Biology respectively.
# Hypothesis: Shekar scored 76, 65, 82, 67 and 85 marks in Mathematics, Science, Social studies, English and Biology respectively.
# Golden Label: neutral

# defining the marks for each subject in premise
math_premise = 46
science_premise = 65
social_studies_premise = 82
english_premise = 67
biology_premise = 85

# defining the marks for each subject in hypothesis
math_hypothesis = 76
science_hypothesis = 65
social_studies_hypothesis = 82
english_hypothesis = 67
biology_hypothesis = 85

# checking if the marks in hypothesis are less than or equal to the marks in the premise
if math_hypothesis <= math_premise or science_hypothesis < science_premise or social_studies_hypothesis < social_studies_premise or english_hypothesis < english_premise or biology_hypothesis < biology_premise:
    label = "contradiction"
# checking if the marks in hypothesis are equal to the marks in the premise
elif math_hypothesis == math_premise and science_hypothesis == science_premise and social_studies_hypothesis == social_studies_premise and english_hypothesis == english_premise and biology_hypothesis == biology_premise:
    label = "entailment"
else:
    # any marks greater than the marks in the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

