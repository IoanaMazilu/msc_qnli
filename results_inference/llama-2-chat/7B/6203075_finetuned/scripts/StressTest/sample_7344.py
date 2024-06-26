percent_price_change_premise = 28
percent_price_change_hypothesis = 68

# the hypothesis refers to the percentage price change of crude oil mentioned in the premise
if percent_price_change_hypothesis < percent_price_change_premise:
    # check if the hypothesis value contradicts the percentage price change in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
