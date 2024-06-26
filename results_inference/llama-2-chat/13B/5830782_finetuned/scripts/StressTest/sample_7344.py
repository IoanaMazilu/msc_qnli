oil_price_change_premise = 28
oil_price_change_hypothesis = 68
oil_price_increase_premise = 5
oil_price_increase_hypothesis = 5

# the hypothesis refers to the price change and increase of crude oil mentioned in the premise
if oil_price_change_hypothesis < oil_price_change_premise:
    # check if the estimate of 'oil_price_change_hypothesis' contradicts the price change in the premise
    label = "contradiction"
elif oil_price_increase_hypothesis!= oil_price_increase_premise:
    # check if the price increase in the hypothesis contradicts the price increase reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
