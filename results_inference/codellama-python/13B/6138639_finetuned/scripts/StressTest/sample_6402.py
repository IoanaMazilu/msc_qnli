components_premise = 60
components_hypothesis = 30
machine_A_premise = 80
machine_A_hypothesis = 80
machine_B_premise = 20
machine_B_hypothesis = 20

# the hypothesis refers to the number of components and the percentage of components manufactured by Machine A and B, mentioned in the premise
if components_hypothesis <= components_premise:
    # check if the estimate of 'components_hypothesis' contradicts the number of components in the premise
    label = "contradiction"
elif machine_A_hypothesis!= machine_A_premise or machine_B_hypothesis!= machine_B_premise:
    # check if the percentage of components manufactured by Machine A and B in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
