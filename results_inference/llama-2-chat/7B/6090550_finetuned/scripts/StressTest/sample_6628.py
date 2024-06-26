 score_less_than_8_premise = 8
score_less_than_2_premise = 2
score_less_than_3_premise = 3

score_less_than_8_hypothesis = 8
score_less_than_2_hypothesis = 2
score_less_than_3_hypothesis = 3

# the hypothesis talks about the scores Mary got, which are also mentioned in the premise
if score_less_than_8_hypothesis!= score_less_than_8_premise or score_less_than_2_hypothesis!= score_less_than_2_premise or score_less_than_3_hypothesis!= score_less_than_3_premise:
    # check if the scores in the hypothesis contradict the scores in the premise
    label = "contradiction"
else:
    # if the scores in the hypothesis do not contradict the scores in the premise, we can infer entailment
    label = "entailment"

print(label)
