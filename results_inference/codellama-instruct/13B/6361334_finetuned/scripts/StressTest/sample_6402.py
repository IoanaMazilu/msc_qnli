components_premise = 60
components_hypothesis = 30

# the hypothesis refers to the number of components that a factory must manufacture
# the premise mentions the number of components that can be manufactured by Machine A and Machine B
if components_hypothesis <= components_premise:
    # check if the hypothesis value contradicts the number of components in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of components that can be manufactured by Machine A and Machine B
    # any number of components greater than 'components_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
