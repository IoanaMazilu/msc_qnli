car_ac_ratio_premise = 3/2
car_ac_ratio_hypothesis = 8/2

# the hypothesis refers to the ratio of car and AC prices mentioned in the premise
if car_ac_ratio_hypothesis == car_ac_ratio_premise:
    # check if the ratio in the hypothesis matches the ratio reported in the premise
    label = "entailment"
elif car_ac_ratio_hypothesis!= car_ac_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
