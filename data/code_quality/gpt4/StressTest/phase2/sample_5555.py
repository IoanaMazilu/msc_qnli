kunal_sagar_ratio_premise = 6/5
kunal_sagar_ratio_hypothesis = 6/5

# the hypothesis refers to the ratio of ages of Kunal and Sagar mentioned in the premise
if kunal_sagar_ratio_hypothesis > kunal_sagar_ratio_premise:
    # check if the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif kunal_sagar_ratio_hypothesis < kunal_sagar_ratio_premise:
    # check if the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis ratio is equal to the premise ratio, we can infer entailment
    label = "entailment"

print(label)
