components_premise = 30
components_hypothesis = 60
percent_A_premise = 80
percent_A_hypothesis = 80
percent_B_premise = 20
percent_B_hypothesis = 20

# the hypothesis refers to the number of components mentioned in the premise
if components_hypothesis!= components_premise:
    # check if the number of components in the hypothesis contradicts the number of components reported in the premise
    label = "contradiction"
elif percent_A_hypothesis!= percent_A_premise or percent_B_hypothesis!= percent_B_premise:
    # check if the estimates of the percentage of components manufactured by Machine A and Machine B in the hypothesis contradict the estimates in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
