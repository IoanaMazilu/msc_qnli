miami_kennedy_ratio_premise = 8/2
miami_kennedy_ratio_hypothesis = 1/2
miami_logan_ratio_premise = 4
miami_logan_ratio_hypothesis = 4

# the hypothesis refers to the ratios of passengers using Miami, Kennedy, and Logan airports, mentioned in the premise
if miami_kennedy_ratio_hypothesis!= miami_kennedy_ratio_premise:
    # check if the ratio of passengers using Miami and Kennedy airports in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif miami_logan_ratio_hypothesis!= miami_logan_ratio_premise:
    # check if the ratio of passengers using Miami and Logan airports in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis ratios do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
