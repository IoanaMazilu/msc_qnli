car_ac_price_ratio_premise = 3/2
car_ac_price_ratio_hypothesis = 8/2

# the hypothesis refers to the ratio of the price of a car and AC mentioned in the premise
if car_ac_price_ratio_hypothesis!= car_ac_price_ratio_premise:
    # check if the ratio of the price of a car and AC in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
