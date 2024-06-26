socre_amar_premise = 64
score_amar_hypothesis = 84
score_bhavan_premise = 36
score_bhavan_hypothesis = 36
score_chetan_premise = 44
score_chetan_hypothesis = 44

# the hypothesis refers to the scores of Amar, Bhavan and Chetan mentioned in the premise
if score_amar_premise > score_amar_hypothesis:
    # check if the score of Amar in the hypothesis contradicts the score of Amar in the premise
    label = "contradiction"
elif score_bhavan_premise!= score_bhavan_hypothesis:
    # check if the score of Bhavan in the hypothesis contradicts the score of Bhavan in the premise
    label = "contradiction"
elif score_chetan_premise!= score_chetan_hypothesis:
    # check if the score of Chetan in the hypothesis contradicts the score of Chetan in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
