price_drop_premise = 68
price_drop_hypothesis = 28
price_increase_premise = 5
price_increase_hypothesis = 5

# the hypothesis refers to the price drop and increase mentioned in the premise
if price_drop_hypothesis > price_drop_premise:
    # check if the percentage of price drop in the hypothesis contradicts the percentage of price drop in the premise
    label = "contradiction"
elif price_increase_hypothesis!= price_increase_premise:
    # check if the percentage of price increase in the hypothesis contradicts the percentage of price increase in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of price drop
    # any percentage of price drop less than 'price_drop_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
