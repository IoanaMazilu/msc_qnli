premise_share = 6970
hypothesis_share = 1970

# the hypothesis refers to the share of Sameer in the profit
if hypothesis_share > premise_share:
    # check if the estimate of 'hypothesis_share' contradicts the premise
    label = "contradiction"
elif hypothesis_share == premise_share:
    # check if the hypothesis value is consistent with the premise
    label = "neutral"
else:
    # the premise gives only an estimate for the share of Sameer
    # any share greater than 'premise_share' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
