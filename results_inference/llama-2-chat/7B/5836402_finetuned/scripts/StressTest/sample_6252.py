scores_premise = [1, 2, 3, 4]
scores_hypothesis = [7, 2, 3, 4]

# the hypothesis refers to the scores mentioned in the premise
if scores_hypothesis[0] <= scores_premise[0]:
    # check if the estimate of'scores_hypothesis[0]" contradicts the minimum score in the premise
    label = "contradiction"
elif scores_hypothesis[1]!= scores_premise[1]:
    # check if the score in the hypothesis contradicts the score in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
