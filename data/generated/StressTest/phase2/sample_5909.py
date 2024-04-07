# Premise: Shekar scored 76, 65, 82, 67 and 75 marks in Mathematics, Science, Social studies, English and Biology respectively.
# Hypothesis: Shekar scored more than 76, 65, 82, 67 and 75 marks in Mathematics, Science, Social studies, English and Biology respectively.
# Golden Label: contradiction

math_marks_premise = 76
science_marks_premise = 65
social_studies_marks_premise = 82
english_marks_premise = 67
biology_marks_premise = 75

math_marks_hypothesis = 76
science_marks_hypothesis = 65
social_studies_marks_hypothesis = 82
english_marks_hypothesis = 67
biology_marks_hypothesis = 75

# the hypothesis refers to the marks of Shekar in various subjects mentioned in the premise
if math_marks_hypothesis > math_marks_premise or science_marks_hypothesis > science_marks_premise or social_studies_marks_hypothesis > social_studies_marks_premise or english_marks_hypothesis > english_marks_premise or biology_marks_hypothesis > biology_marks_premise:
    # check if the scores in the hypothesis are greater than the scores in the premise
    label = "contradiction"
else:
    # if the scores in the hypothesis are not more than the scores in the premise, we can infer entailment
    label = "entailment"

print(label)

