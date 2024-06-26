price_slump_premise = 68
price_slump_hypothesis = 28

# the hypothesis refers to the price slump mentioned in the premise
if price_slump_hypothesis <= price_slump_premise:
    # check if the hypothesis value contradicts the estimate of less than 'price_slump_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the price slump
    # any price slump greater than 'price_slump_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
