total_components_premise = 60
total_components_hypothesis = 60
percentage_machineA_premise = 80
percentage_machineA_hypothesis = 80
percentage_machineB_premise = 20
percentage_machineB_hypothesis = 20

# the hypothesis talks about the total number of electronics components and the percentage of components to be manufactured by machine A and B 
# referenced also in the premise
if total_components_hypothesis >= total_components_premise:
    # check if the total number of components in the hypothesis contradicts the premise
    label = "contradiction"
elif percentage_machineA_hypothesis != percentage_machineA_premise or percentage_machineB_hypothesis != percentage_machineB_premise:
    # check if the number of components to be manufactured by machine A and B in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
