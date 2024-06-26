car_ac_ratio_premise = 3/2
car_ac_ratio_hypothesis = 8/2

# the hypothesis refers to the same ratio of the price of a car and AC as the premise
if car_ac_ratio_hypothesis!= car_ac_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the ratio in the hypothesis does not contradict the ratio in the premise, we can infer entailment
    label = "entailment"

print(label)
