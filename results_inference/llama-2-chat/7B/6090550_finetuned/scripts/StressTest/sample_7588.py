average_score_premise = 46
scores_premise = [75, 72, 63, 65]

average_score_hypothesis = 86
scores_hypothesis = [75, 72, 63, 65]

# the hypothesis refers to the same scores and average score as the premise
if average_score_hypothesis!= average_score_premise:
    # check if the average score in the hypothesis contradicts the average score reported in the premise
    label = "contradiction"
elif scores_hypothesis!= scores_premise:
    # check if the scores in the hypothesis contradict the scores in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
