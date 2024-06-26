components_premise = 30
components_hypothesis = 60

# the hypothesis refers to the number of components mentioned in the premise
if components_hypothesis <= components_premise:
    # check if the number of components in the hypothesis contradicts the estimate of more than 'components_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of components
    # any number of components greater than 'components_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
