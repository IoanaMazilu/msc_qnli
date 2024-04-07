# Premise: Of the more than 30 electronics components that a factory must manufacture, 50 percent would be most e ¢ ciently manufactured by Machine A and the remaining 50 percent would be most efficiently manufactured by Machine B, though either machine could manufacture any of the 90 components.
# Hypothesis: Of the 90 electronics components that a factory must manufacture, 50 percent would be most e ¢ ciently manufactured by Machine A and the remaining 50 percent would be most efficiently manufactured by Machine B, though either machine could manufacture any of the 90 components.
# Golden Label: neutral

components_premise = 30
components_hypothesis = 90
percent_machineA_premise = 50
percent_machineB_premise = 50
percent_machineA_hypothesis = 50
percent_machineB_hypothesis = 50

# the hypothesis refers to the number of components and their distribution between the machines
if components_hypothesis <= components_premise:
    # check if the number of components in the hypothesis contradicts the estimate of more than 'components_premise'
    label = "contradiction"
elif percent_machineA_hypothesis != percent_machineA_premise or percent_machineB_hypothesis != percent_machineB_premise:
    # check if the percentage of components assigned to machines A or B in the hypothesis contradicts the percentages in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of components
    # any number of components greater than 'components_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

