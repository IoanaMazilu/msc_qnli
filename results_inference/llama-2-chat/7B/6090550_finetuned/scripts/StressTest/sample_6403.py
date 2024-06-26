components_premise = 30
components_hypothesis = 60
machine_a_percentage_premise = 0.8
machine_b_percentage_premise = 0.2
machine_a_percentage_hypothesis = 0.8
machine_b_percentage_hypothesis = 0.2

# the hypothesis refers to the percentage of components that would be most efficiently manufactured by each machine, which is also mentioned in the premise
if components_hypothesis <= components_premise:
    # check if the number of components in the hypothesis contradicts the number of components in the premise
    label = "contradiction"
elif machine_a_percentage_hypothesis!= machine_a_percentage_premise or machine_b_percentage_hypothesis!= machine_b_percentage_premise:
    # check if the percentage of components manufactured by each machine in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
