min_scores_premise = [7, 2, 3, 4]
max_scores_premise = [1, 2, 3, 4]

# the hypothesis refers to the minimum and maximum scores mentioned in the premise
if min_scores_hypothesis >= min_scores_premise:
    # check if the minimum scores in the hypothesis contradict the minimum scores in the premise
    label = "contradiction"
elif max_scores_hypothesis <= max_scores_premise:
    # check if the maximum scores in the hypothesis contradict the maximum scores in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
