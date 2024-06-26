price_slump_premise = 68
price_slump_hypothesis = 28
price_increase_premise = 5
price_increase_hypothesis = 5

# the hypothesis refers to the percentage of price slump and increase in the premise
if price_slump_hypothesis >= price_slump_premise:
    # check if the hypothesis value contradicts the estimate of less than 'price_slump_premise'
    label = "contradiction"
elif price_increase_hypothesis!= price_increase_premise:
    # check if the percentage of price increase in the hypothesis contradicts the percentage of price increase reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of price slump
    # any percentage of price slump less than 'price_slump_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
