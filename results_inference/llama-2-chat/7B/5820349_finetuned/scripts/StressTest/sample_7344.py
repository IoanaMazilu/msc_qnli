price_change_premise = 28
price_change_hypothesis = 68
price_increase_premise = 5
price_increase_hypothesis = 5

# the hypothesis refers to the price change and expected price increase in the next month mentioned in the premise
if price_change_hypothesis < price_change_premise:
    # check if the estimate of 'price_change_hypothesis' contradicts the price change in the premise
    label = "contradiction"
elif price_increase_hypothesis!= price_increase_premise:
    # check if the expected price increase in the hypothesis contradicts the expected price increase reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
