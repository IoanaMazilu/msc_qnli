price_change_premise = 5
price_change_hypothesis = 5
price_change_premise_months = 3
price_change_hypothesis_months = 3

# the hypothesis refers to the price change and time period mentioned in the premise
if price_change_hypothesis >= price_change_premise:
    # check if the estimate of 'price_change_hypothesis' contradicts the price change in the premise
    label = "contradiction"
elif price_change_hypothesis < price_change_premise_months:
    # check if the estimate of 'price_change_hypothesis' contradicts the time period in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
