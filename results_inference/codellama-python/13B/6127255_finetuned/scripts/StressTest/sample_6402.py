components_premise = 60
components_hypothesis = 30
machineA_premise = 80
machineA_hypothesis = 80
machineB_premise = 20
machineB_hypothesis = 20

# the hypothesis refers to the same number of components, the same percentage of components manufactured by Machine A, and the same percentage of components manufactured by Machine B
if components_hypothesis >= components_premise:
    # check if the number of components in the hypothesis contradicts the number of components in the premise
    label = "contradiction"
elif machineA_hypothesis!= machineA_premise or machineB_hypothesis!= machineB_premise:
    # check if the percentage of components manufactured by Machine A or Machine B in the hypothesis contradicts the percentages in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
