components_premise = 30
components_hypothesis = 60
machine_A_premise = 80
machine_A_hypothesis = 80
machine_B_premise = 20
machine_B_hypothesis = 20

# the hypothesis refers to the number of components, the percentage of components that Machine A and B would manufacture, and the distribution of components between the machines
if components_hypothesis <= components_premise:
    # check if the number of components in the hypothesis contradicts the estimate of more than 'components_premise'
    label = "contradiction"
elif machine_A_hypothesis!= machine_A_premise or machine_B_hypothesis!= machine_B_premise:
    # check if the percentage of components that Machine A and B would manufacture in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of components
    # any number of components greater than 'components_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
