price_car_premise = 3
price_ac_premise = 2
price_car_hypothesis = 8
price_ac_hypothesis = 2

# the hypothesis refers to the ratio of the price of a car and AC, which is also mentioned in the premise
if price_car_hypothesis / price_ac_hypothesis!= price_car_premise / price_ac_premise:
    # check if the ratio of the price of a car and AC in the hypothesis contradicts the ratio mentioned in the premise
    label = "contradiction"
else:
    # if the ratio in the hypothesis is consistent with the ratio in the premise, we can infer entailment
    label = "entailment"

print(label)
