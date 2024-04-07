# Premise: Tanya is more than 10% more efficient than Sakshi.
# Hypothesis: Tanya is 20% more efficient than Sakshi.
# Golden Label: neutral

efficiency_difference_premise = 10
efficiency_difference_hypothesis = 20

# the hypothesis talks about the efficiency difference between Tanya and Sakshi, referenced also in the premise
if efficiency_difference_hypothesis <= efficiency_difference_premise:
    # check if the hypothesis value contradicts the estimate of more than 'efficiency_difference_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the efficiency difference
    # any efficiency difference greater than 'efficiency_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

