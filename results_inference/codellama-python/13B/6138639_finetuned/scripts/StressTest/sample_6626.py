sheep_to_horses_ratio_premise = 6/7
sheep_to_horses_ratio_hypothesis = 6/7

# the hypothesis refers to the ratio between the number of sheep and the number of horses mentioned in the premise
if sheep_to_horses_ratio_hypothesis >= sheep_to_horses_ratio_premise:
    # check if the hypothesis value contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
