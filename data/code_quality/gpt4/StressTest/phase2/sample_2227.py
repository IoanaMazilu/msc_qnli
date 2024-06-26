miami_kennedy_ratio_premise = 7/2
miami_kennedy_ratio_hypothesis = 1/2
miami_logan_ratio_premise = 4
miami_logan_ratio_hypothesis = 4

# the hypothesis refers to the same ratios of passengers between airports as in the premise
if miami_kennedy_ratio_hypothesis != miami_kennedy_ratio_premise:
    # check if the Miami/Kennedy ratio in the hypothesis contradicts the one in the premise
    label = "contradiction"
elif miami_logan_ratio_hypothesis != miami_logan_ratio_premise:
    # check if the Miami/Logan ratio in the hypothesis contradicts the one in the premise
    label = "contradiction"
else:
    # if the ratios in the hypothesis do not contradict the ones in the premise, we can infer entailment
    label = "entailment"

print(label)
