components_premise = 60
components_hypothesis = 60
percentage_machine_a_premise = 80
percentage_machine_b_premise = 20
percentage_machine_a_hypothesis = 80
percentage_machine_b_hypothesis = 20

# the hypothesis refers to the number of components and the percentage of each component that is most efficiently manufactured by Machine A and Machine B
if components_hypothesis!= components_premise:
    # check if the number of components in the hypothesis contradicts the number of components reported in the premise
    label = "contradiction"
elif percentage_machine_a_hypothesis!= percentage_machine_a_premise:
    # check if the percentage of components most efficiently manufactured by Machine A in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
elif percentage_machine_b_hypothesis!= percentage_machine_b_premise:
    # check if the percentage of components most efficiently manufactured by Machine B in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
