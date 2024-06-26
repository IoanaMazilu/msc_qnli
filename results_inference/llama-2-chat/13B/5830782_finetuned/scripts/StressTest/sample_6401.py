miami_kennedy_ratio_premise = 1/2
miami_kennedy_ratio_hypothesis = 3/2
miami_logan_ratio_premise = 4
miami_logan_ratio_hypothesis = 4

# the hypothesis refers to the ratios of passengers between Miami, Kennedy, and Logan airports mentioned in the premise
if miami_kennedy_ratio_premise!= miami_kennedy_ratio_hypothesis:
    # check if the Miami-Kennedy ratio in the hypothesis contradicts the Miami-Kennedy ratio reported in the premise
    label = "contradiction"
elif miami_logan_ratio_premise!= miami_logan_ratio_hypothesis:
    # check if the Miami-Logan ratio in the hypothesis contradicts the Miami-Logan ratio reported in the premise
    label = "contradiction"
else:
    # if the hypothesis ratios do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
