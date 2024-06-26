price_drop_premise = 28
price_drop_hypothesis = 68
price_increase_premise = 5
price_increase_hypothesis = 5

# the hypothesis refers to the price drop and increase of crude oil mentioned in the premise
if price_drop_premise >= price_drop_hypothesis:
    # check if the estimate of 'price_drop_hypothesis' contradicts the price drop in the premise
    label = "contradiction"
elif price_increase_hypothesis!= price_increase_premise:
    # check if the price increase in the hypothesis contradicts the price increase reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
