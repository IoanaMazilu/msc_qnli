premise_share = 1300
hypothesis_share = 4300

# the hypothesis refers to the number of shares mentioned in the premise
if hypothesis_share <= premise_share:
    # check if the estimate of 'hypothesis_share' contradicts the number of shares in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of shares
    # any number of shares greater than 'premise_share' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
