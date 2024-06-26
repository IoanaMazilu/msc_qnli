total_components_premise = 90
total_components_hypothesis = 30
components_machine_A_premise = total_components_premise * 0.5
components_machine_B_premise = total_components_premise * 0.5
components_machine_A_hypothesis = total_components_hypothesis * 0.5
components_machine_B_hypothesis = total_components_hypothesis * 0.5

# the hypothesis refers to the same machines and process described in the premise, but gives a different total number of components
if total_components_hypothesis > total_components_premise:
    # check if the hypothesis total contradicts the premise
    label = "contradiction"
elif components_machine_A_hypothesis != components_machine_A_premise or components_machine_B_hypothesis != components_machine_B_premise:
    # check if the number of components for machine A or machine B in the hypothesis contradicts the numbers in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
