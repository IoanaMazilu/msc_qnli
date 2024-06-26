sheep_to_horse_ratio_premise = 6/7
sheep_to_horse_ratio_hypothesis = 6/7

# the hypothesis refers to the same ratio of sheep to horses as in the premise
if sheep_to_horse_ratio_premise <= sheep_to_horse_ratio_hypothesis:
    # check if the estimate of'sheep_to_horse_ratio_hypothesis' contradicts the ratio in the premise
    label = "contradiction"
elif sheep_to_horse_ratio_hypothesis > sheep_to_horse_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
