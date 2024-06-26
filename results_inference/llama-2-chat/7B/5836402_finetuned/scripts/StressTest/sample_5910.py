sheep_to_horse_ratio_premise = 1/7
sheep_to_horse_ratio_hypothesis = 6/7

# the hypothesis refers to the ratio of sheep to horses, which is also mentioned in the premise
if sheep_to_horse_ratio_hypothesis >= sheep_to_horse_ratio_premise:
    # check if the estimate of'sheep_to_horse_ratio_hypothesis' contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise ratio, we can infer entailment
    label = "entailment"

print(label)
