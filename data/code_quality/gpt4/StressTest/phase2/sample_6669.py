efficiency_suresh_premise = 25
efficiency_suresh_hypothesis = 35

# the hypothesis refers to Suresh's efficiency in comparison with Kamal's, mentioned in the premise
if efficiency_suresh_hypothesis <= efficiency_suresh_premise:
    # check if the hypothesis value contradicts the estimate of 'efficiency_suresh_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the Suresh's efficiency
    # any efficiency percentage greater than 'efficiency_suresh_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
