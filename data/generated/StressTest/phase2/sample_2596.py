# Premise: Rosy is more than 10% more efficient than Mary.
# Hypothesis: Rosy is 30% more efficient than Mary.
# Golden Label: neutral

efficiency_premise = 10
efficiency_hypothesis = 30

# the hypothesis talks about the efficiency of Rosy compared to Mary, referenced also in the premise
if efficiency_hypothesis <= efficiency_premise:
    # check if the hypothesis value contradicts the estimate of more than 'efficiency_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the efficiency
    # any efficiency greater than 'efficiency_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

