# Premise: Shekar scored more than 46, 65, 82, 67 and 75 marks in Mathematics, Science, Social studies, English and Biology respectively.
# Hypothesis: Shekar scored 76, 65, 82, 67 and 75 marks in Mathematics, Science, Social studies, English and Biology respectively.
# Golden Label: neutral

math_score_premise = 46
science_score_premise = 65
social_studies_score_premise = 82
english_score_premise = 67
biology_score_premise = 75

math_score_hypothesis = 76
science_score_hypothesis = 65
social_studies_score_hypothesis = 82
english_score_hypothesis = 67
biology_score_hypothesis = 75

# the hypothesis gives exact marks scored by Shekar in each subject which are also mentioned in the premise
if math_score_hypothesis <= math_score_premise or science_score_hypothesis <= science_score_premise or social_studies_score_hypothesis <= social_studies_score_premise or english_score_hypothesis <= english_score_premise or biology_score_hypothesis <= biology_score_premise:
    # check if any of the hypothesis values contradict the estimate of more than the respective subject's score in the premise
    label = "contradiction"
elif math_score_hypothesis == math_score_premise + 30 and science_score_hypothesis == science_score_premise and social_studies_score_hypothesis == social_studies_score_premise and english_score_hypothesis == english_score_premise and biology_score_hypothesis == biology_score_premise:
    # the premise gives only an estimate for the marks
    # if the hypothesis gives the exact marks and they match with the premise, then it is an entailment
    label = "entailment"
else:
    # the premise gives only an estimate for the marks
    # any number of marks greater than the premise's estimate is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

