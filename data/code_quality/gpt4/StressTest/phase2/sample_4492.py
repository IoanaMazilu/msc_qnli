efficiency_premise = 45
efficiency_hypothesis = 25

# the hypothesis refers to the efficiency of Tanya compared to Sakshi, also mentioned in the premise
if efficiency_hypothesis > efficiency_premise:
    # check if the 'efficiency_hypothesis' contradicts the estimate of less than 'efficiency_premise' 
    label = "contradiction"
elif efficiency_hypothesis < efficiency_premise:
    # if 'efficiency_hypothesis' is less than 'efficiency_premise', we can infer entailment
    label = "entailment"
else:
    # the premise gives an estimate for the efficiency
    # the exact efficiency from the hypothesis cannot be explicitly entailed from the premise, hence it's neutral
    label = "neutral"

print(label)
