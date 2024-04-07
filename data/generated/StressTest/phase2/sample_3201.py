# Premise: Shekar scored 76, 65, 82, 67 and 85 marks in Mathematics, Science, Social studies, English and Biology respectively.
# Hypothesis: Shekar scored more than 46, 65, 82, 67 and 85 marks in Mathematics, Science, Social studies, English and Biology respectively.
# Golden Label: entailment

math_marks_premise = 76
math_marks_hypothesis = 46
science_marks_premise = 65
science_marks_hypothesis = 65
social_studies_marks_premise = 82
social_studies_marks_hypothesis = 82
english_marks_premise = 67
english_marks_hypothesis = 67
biology_marks_premise = 85
biology_marks_hypothesis = 85

# the hypothesis refers to the marks scored by Shekar in various subjects mentioned in the premise
if math_marks_hypothesis > math_marks_premise or science_marks_hypothesis > science_marks_premise or social_studies_marks_hypothesis > social_studies_marks_premise or english_marks_hypothesis > english_marks_premise or biology_marks_hypothesis > biology_marks_premise:
    # check if the hypothesis values contradict the marks reported in the premise
    label = "contradiction"
elif math_marks_hypothesis < math_marks_premise and science_marks_hypothesis == science_marks_premise and social_studies_marks_hypothesis == social_studies_marks_premise and english_marks_hypothesis == english_marks_premise and biology_marks_hypothesis == biology_marks_premise:
    # if the hypothesis values do not contradict the premise ones, and one value is explicitly less than the corresponding premise value, we can infer entailment
    label = "entailment"
else:
    # any other situation is considered neutral
    label = "neutral"

print(label)

