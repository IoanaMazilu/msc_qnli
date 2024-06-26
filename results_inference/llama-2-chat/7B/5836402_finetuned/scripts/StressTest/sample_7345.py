price_drop_premise = 68
price_drop_hypothesis = 28
expected_increase_premise = 5
expected_increase_hypothesis = 5

# the hypothesis refers to the price drop and expected increase of crude oil mentioned in the premise
if price_drop_hypothesis >= price_drop_premise:
    # check if the estimate of 'price_drop_hypothesis' contradicts the number of price drop in the premise
    label = "contradiction"
elif expected_increase_hypothesis!= expected_increase_premise:
    # check if the expected increase in the hypothesis contradicts the expected increase in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
