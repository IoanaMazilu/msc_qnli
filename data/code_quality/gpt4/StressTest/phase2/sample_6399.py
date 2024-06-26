miami_kennedy_ratio_premise = 1/2
miami_kennedy_ratio_hypothesis = 8/2
miami_logan_ratio_premise = 4
miami_logan_ratio_hypothesis = 4

# the hypothesis refers to the ratio of passengers between Miami and Kennedy and Miami and Logan airports mentioned in the premise
if miami_kennedy_ratio_hypothesis <= miami_kennedy_ratio_premise:
    # check if the ratio of passengers between Miami and Kennedy in the hypothesis contradicts the ratio mentioned in the premise
    label = "contradiction"
elif miami_logan_ratio_hypothesis != miami_logan_ratio_premise:
    # check if the ratio of passengers between Miami and Logan in the hypothesis contradicts the ratio mentioned in the premise
    label = "contradiction"
else:
    # if the ratios in the hypothesis do not contradict the ratios in the premise, we can infer entailment
    label = "entailment"

print(label)