scores_premise = [1, 2, 3, 4, 5]
scores_hypothesis = [8, 2, 3, 4, 5]

# the hypothesis refers to the scores mentioned in the premise
if len(scores_hypothesis)!= len(scores_premise):
    # check if the number of scores in the hypothesis contradicts the number of scores in the premise
    label = "contradiction"
elif scores_hypothesis[0] <= scores_premise[0]:
    # check if the first score in the hypothesis contradicts the first score in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
