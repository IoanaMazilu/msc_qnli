car_price_premise = 2
ac_price_premise = 2
car_price_hypothesis = 3
ac_price_hypothesis = 2

# the hypothesis refers to the ratio of the price of a car and AC, which is also mentioned in the premise
if car_price_hypothesis / ac_price_hypothesis!= car_price_premise / ac_price_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the ratio in the hypothesis is consistent with the ratio in the premise, we can infer entailment
    label = "entailment"

print(label)
