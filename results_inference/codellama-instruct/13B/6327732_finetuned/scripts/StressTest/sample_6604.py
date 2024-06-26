investment_premise = 3
investment_hypothesis = 2

# the hypothesis refers to the number of times the original investment is returned
if investment_hypothesis <= investment_premise:
    # check if the estimate of 'investment_hypothesis' contradicts the number of times the original investment is returned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of times the original investment is returned
    # any number of times greater than 'investment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
