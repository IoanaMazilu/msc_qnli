investment_premise = 2
investment_hypothesis = 3

# the hypothesis refers to the multiple of investment gained at the end of 'n' years, also mentioned in the premise
if investment_hypothesis <= investment_premise:
    # check if the estimate of 'investment_hypothesis' contradicts the multiple of investment gained in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the multiple of investment gained
    # any multiple of investment greater than 'investment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
