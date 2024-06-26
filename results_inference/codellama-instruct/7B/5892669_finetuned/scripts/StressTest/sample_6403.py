components_premise = 30
components_hypothesis = 60
machine_a_premise = 80
machine_a_hypothesis = 80
machine_b_premise = 20
machine_b_hypothesis = 20

# the hypothesis refers to the number of components, the percentage of components that Machine A and Machine B can manufacture, and the remaining components that can be manufactured by either machine
if components_premise >= components_hypothesis:
    # check if the number of components in the hypothesis contradicts the estimate of more than 'components_premise'
    label = "contradiction"
elif machine_a_premise!= machine_a_hypothesis or machine_b_premise!= machine_b_hypothesis:
    # check if the percentage of components that Machine A and Machine B can manufacture in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of components
    # any number of components greater than 'components_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
