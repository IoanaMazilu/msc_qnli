# Premise: Shekar scored less than 86, 65, 82, 67 and 55 marks in Mathematics, Science, Social studies, English and Biology respectively.
# Hypothesis: Shekar scored 76, 65, 82, 67 and 55 marks in Mathematics, Science, Social studies, English and Biology respectively.
# Golden Label: neutral

math_marks_premise = 86
science_marks_premise = 65
social_studies_marks_premise = 82
english_marks_premise = 67
biology_marks_premise = 55

math_marks_hypothesis = 76
science_marks_hypothesis = 65
social_studies_marks_hypothesis = 82
english_marks_hypothesis = 67
biology_marks_hypothesis = 55

# the hypothesis claims specific marks for each subject, which are also mentioned in the premise
if math_marks_hypothesis >= math_marks_premise or science_marks_hypothesis > science_marks_premise or social_studies_marks_hypothesis >= social_studies_marks_premise or english_marks_hypothesis > english_marks_premise or biology_marks_hypothesis > biology_marks_premise:
    # check if the hypothesis marks contradict the estimates of less than the respective premise marks
    label = "contradiction"
elif math_marks_hypothesis < math_marks_premise and science_marks_hypothesis == science_marks_premise and social_studies_marks_hypothesis == social_studies_marks_premise and english_marks_hypothesis == english_marks_premise and biology_marks_hypothesis == biology_marks_premise:
    # if the hypothesis marks are less than or equal to the premise ones, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis marks do not contradict the premise ones, but cannot be explicitly entailed from the premise, we infer neutrality
    label = "neutral"

print(label)

