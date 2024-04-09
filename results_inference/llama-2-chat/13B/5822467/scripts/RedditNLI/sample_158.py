factors_premise = "5"
factors_hypothesis = "5"

# the premise and hypothesis mention the number of factors contributing to the US economy's success
if factors_premise!= factors_hypothesis:
    # check if the number of factors in the hypothesis contradicts the number of factors in the premise
    label = "contradiction"
elif factors_hypothesis > factors_premise:
    # check if the number of factors in the hypothesis is greater than the number of factors in the premise
    label = "entailment"
else:
    # the premise gives only an estimate for the number of factors
    # any estimate of the number of factors in the hypothesis greater or equal to the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
