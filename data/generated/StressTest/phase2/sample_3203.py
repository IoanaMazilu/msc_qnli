# Premise: Shekar scored 76, 65, 82, 67 and 85 marks in Mathematics, Science, Social studies, English and Biology respectively.
# Hypothesis: Shekar scored more than 76, 65, 82, 67 and 85 marks in Mathematics, Science, Social studies, English and Biology respectively.
# Golden Label: contradiction

math_marks_premise = 76
science_marks_premise = 65
social_studies_marks_premise = 82
english_marks_premise = 67
biology_marks_premise = 85

math_marks_hypothesis = 76
science_marks_hypothesis = 65
social_studies_marks_hypothesis = 82
english_marks_hypothesis = 67
biology_marks_hypothesis = 85

# the hypothesis talks about the marks scored by Shekar in various subjects, referenced also in the premise
if math_marks_hypothesis <= math_marks_premise or science_marks_hypothesis <= science_marks_premise or social_studies_marks_hypothesis <= social_studies_marks_premise or english_marks_hypothesis <= english_marks_premise or biology_marks_hypothesis <= biology_marks_premise:
    # check if the hypothesis values contradict the estimated marks scored in the premise
    label = "contradiction"
else:
    # the premise gives exact marks scored
    # any marks greater than the marks given in the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

