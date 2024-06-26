sheep_to_horse_ratio_premise = 1/7
sheep_to_horse_ratio_hypothesis = 6/7

# the hypothesis refers to the sheep to horse ratio, which is also mentioned in the premise
if sheep_to_horse_ratio_hypothesis!= sheep_to_horse_ratio_premise:
    # check if the sheep to horse ratio in the hypothesis contradicts the sheep to horse ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
