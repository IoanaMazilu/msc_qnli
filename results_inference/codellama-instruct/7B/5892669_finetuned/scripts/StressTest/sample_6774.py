ratio_premise = 4/2
ratio_hypothesis = 1/2

# the hypothesis refers to the ratio of distances between A to B and B to C mentioned in the premise
if ratio_hypothesis >= ratio_premise:
    # check if the estimate of 'ratio_hypothesis' contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)