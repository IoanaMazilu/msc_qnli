efficiency_difference_premise = 10
efficiency_difference_hypothesis = 30

# the hypothesis talks about the efficiency difference between Rosy and Mary, referenced also in the premise
if efficiency_difference_premise >= efficiency_difference_hypothesis:
    # check if the premise value contradicts the estimate of less than 'efficiency_difference_hypothesis'
    label = "contradiction"
else:
    # the hypothesis gives only an estimate for the efficiency difference
    # any efficiency difference less than 'efficiency_difference_hypothesis' is consistent with the hypothesis, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
