components_premise = 60
components_hypothesis = 30
percentage_machine_A_premise = 80
percentage_machine_A_hypothesis = 80
percentage_machine_B_premise = 20
percentage_machine_B_hypothesis = 20

# the hypothesis refers to the number of components and the percentage of each machine that manufactures them, mentioned in the premise
if components_hypothesis >= components_premise:
    # check if the number of components in the hypothesis contradicts the number of components reported in the premise
    label = "contradiction"
elif percentage_machine_A_hypothesis!= percentage_machine_A_premise:
    # check if the percentage of Machine A in the hypothesis contradicts the percentage of Machine A reported in the premise
    label = "contradiction"
elif percentage_machine_B_hypothesis!= percentage_machine_B_premise:
    # check if the percentage of Machine B in the hypothesis contradicts the percentage of Machine B reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
