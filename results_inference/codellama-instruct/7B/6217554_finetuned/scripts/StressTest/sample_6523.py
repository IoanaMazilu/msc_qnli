scores_premise = [45, 67, 76, 82, 85]
scores_hypothesis = [55, 67, 76, 82, 85]

# the hypothesis talks about the scores obtained by Reeya, referenced also in the premise
if scores_hypothesis!= scores_premise:
    # check if the scores in the hypothesis contradict the scores reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
