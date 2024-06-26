components_premise = 60
components_hypothesis = 30
machine_a_percentage_premise = 80
machine_a_percentage_hypothesis = 80
machine_b_percentage_premise = 20
machine_b_percentage_hypothesis = 20

# the hypothesis talks about the number of components and the percentage of components that each machine can manufacture
if components_hypothesis!= components_premise:
    # check if the number of components in the hypothesis contradicts the number of components in the premise
    label = "contradiction"
elif machine_a_percentage_hypothesis!= machine_a_percentage_premise or machine_b_percentage_hypothesis!= machine_b_percentage_premise:
    # check if the percentage of components that each machine can manufacture in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
