ram_ratio_premise = 1
raja_ratio_premise = 4
rahim_ratio_premise = 10

ram_ratio_hypothesis = 7
raja_ratio_hypothesis = 4
rahim_ratio_hypothesis = 10

# the hypothesis refers to the same ratios of money distribution between Ram, Raja and Rahim mentioned in the premise
if ram_ratio_hypothesis != ram_ratio_premise or raja_ratio_hypothesis != raja_ratio_premise or rahim_ratio_hypothesis != rahim_ratio_premise:
    # check if any of the three ratios in the hypothesis contradicts the corresponding ratio in the premise
    label = "contradiction"
else:
    # if all the ratios in the hypothesis match those in the premise, we can infer entailment
    label = "entailment"

print(label)
