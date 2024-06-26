french_score_premise = 86
french_score_hypothesis = 86
geography_score_premise = 75
geography_score_hypothesis = 75
art_score_premise = 72
art_score_hypothesis = 72
history_score_premise = 63
history_score_hypothesis = 63
physical_education_score_premise = 65
physical_education_score_hypothesis = 65

# the hypothesis refers to the scores of Adam in different subjects mentioned in the premise
if french_score_hypothesis <= french_score_premise:
    # check if the estimate of 'french_score_hypothesis' contradicts the score in French Language in the premise
    label = "contradiction"
elif geography_score_hypothesis!= geography_score_premise or art_score_hypothesis!= art_score_premise or history_score_hypothesis!= history_score_premise or physical_education_score_hypothesis!= physical_education_score_premise:
    # check if the scores in other subjects in the hypothesis contradict the scores reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
