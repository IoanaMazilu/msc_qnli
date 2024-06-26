math_score_premise = 76
math_score_hypothesis = 46
science_score_premise = 65
science_score_hypothesis = 65
social_studies_score_premise = 82
social_studies_score_hypothesis = 82
english_score_premise = 67
english_score_hypothesis = 67
biology_score_premise = 75
biology_score_hypothesis = 75

# the hypothesis refers to the scores of Shekar in different subjects mentioned in the premise
if math_score_premise <= math_score_hypothesis:
    # check if the estimate of'math_score_hypothesis' contradicts the score in the premise
    label = "contradiction"
elif science_score_premise!= science_score_hypothesis:
    # check if the score in the hypothesis contradicts the score in the premise
    label = "contradiction"
elif social_studies_score_premise!= social_studies_score_hypothesis:
    # check if the score in the hypothesis contradicts the score in the premise
    label = "contradiction"
elif english_score_premise!= english_score_hypothesis:
    # check if the score in the hypothesis contradicts the score in the premise
    label = "contradiction"
elif biology_score_premise!= biology_score_hypothesis:
    # check if the score in the hypothesis contradicts the score in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
