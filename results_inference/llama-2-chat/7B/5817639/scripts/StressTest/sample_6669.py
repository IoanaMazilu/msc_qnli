efficiency_premise = 25
efficiency_hypothesis = 35

# the hypothesis talks about the efficiency of Suresh compared to Kamal
if efficiency_hypothesis <= efficiency_premise:
    # check if the hypothesis value contradicts the estimate of more than 'efficiency_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the efficiency of Suresh compared to Kamal
    # any efficiency greater than 'efficiency_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
