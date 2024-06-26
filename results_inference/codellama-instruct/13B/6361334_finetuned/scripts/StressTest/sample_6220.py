premise_ratio = 4
hypothesis_ratio = 2

# the hypothesis refers to the ratio of money to be divided between Priya, Mani and Rani
if hypothesis_ratio >= premise_ratio:
    # check if the hypothesis value contradicts the estimate of less than 'premise_ratio'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio
    # any ratio less than 'premise_ratio' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
