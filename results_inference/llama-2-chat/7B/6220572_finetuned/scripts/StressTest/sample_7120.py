price_ratio_premise = 2
price_ratio_hypothesis = 3

# the hypothesis refers to the ratio of the price of a car and AC mentioned in the premise
if price_ratio_hypothesis <= price_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of the price
    # any ratio greater than 'price_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
