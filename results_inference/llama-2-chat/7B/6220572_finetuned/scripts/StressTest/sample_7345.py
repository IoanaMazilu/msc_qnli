price_slump_premise = 68
price_slump_hypothesis = 28

# the hypothesis refers to the percentage of price slump in the premise
if price_slump_hypothesis!= price_slump_premise:
    # check if the estimate of 'price_slump_hypothesis' contradicts the percentage of price slump in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of price slump
    # any percentage of price slump less than 'price_slump_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
