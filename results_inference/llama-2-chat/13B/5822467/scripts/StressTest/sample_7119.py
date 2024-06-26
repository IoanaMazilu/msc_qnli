car_price_premise = 3 * 2 = 6
ac_price_premise = 2 * 2 = 4
car_price_hypothesis = 3 * 2 + 1 = 7
ac_price_hypothesis = 2 * 2 + 1 = 5

# the hypothesis refers to the ratio of car and AC prices
if car_price_hypothesis > car_price_premise:
    # check if the estimate of 'car_price_hypothesis' contradicts the ratio reported in the premise
    label = "contradiction"
elif ac_price_hypothesis!= ac_price_premise:
    # check if the estimate of 'ac_price_hypothesis' contradicts the ratio reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
