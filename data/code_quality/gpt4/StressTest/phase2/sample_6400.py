miami_to_kennedy_ratio_premise = 8/2
miami_to_kennedy_ratio_hypothesis = 1/2
miami_to_logan_ratio = 4

# the hypothesis refers to the same ratios of airport users as the premise 
if miami_to_kennedy_ratio_hypothesis != miami_to_kennedy_ratio_premise:
    # check if the ratio of Miami to Kennedy passengers in the hypothesis contradicts the one in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
