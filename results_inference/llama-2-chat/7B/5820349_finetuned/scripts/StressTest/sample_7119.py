car_ac_ratio_premise = 3/2
car_ac_ratio_hypothesis = 2/2

# the hypothesis refers to the ratio of the prices of a car and AC mentioned in the premise
if car_ac_ratio_hypothesis >= car_ac_ratio_premise:
    # check if the estimate of 'car_ac_ratio_hypothesis' contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
