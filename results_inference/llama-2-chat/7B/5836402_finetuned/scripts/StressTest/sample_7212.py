scores_premise = [1, 2, 3, 4, 5]
scores_hypothesis = [8, 2, 3, 4, 5]

# the hypothesis refers to the scores mentioned in the premise
if scores_hypothesis[0] >= scores_premise[0]:
    # check if the lower limit of the scores in the hypothesis contradicts the premise
    label = "contradiction"
elif scores_hypothesis[1]!= scores_premise[1]:
    # check if the score in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
