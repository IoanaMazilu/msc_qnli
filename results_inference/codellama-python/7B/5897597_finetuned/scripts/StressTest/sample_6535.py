miami_to_kennedy_ratio_premise = 7/3
miami_to_kennedy_ratio_hypothesis = 1/3
miami_to_logan_ratio_premise = 4
miami_to_logan_ratio_hypothesis = 4

# the hypothesis refers to the ratios of passengers using Miami, Kennedy and Logan airports, mentioned in the premise
if miami_to_kennedy_ratio_hypothesis!= miami_to_kennedy_ratio_premise:
    # check if the ratio of passengers using Miami to Kennedy in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif miami_to_logan_ratio_hypothesis!= miami_to_logan_ratio_premise:
    # check if the ratio of passengers using Miami to Logan in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the ratios in the hypothesis do not contradict the ratios in the premise, we can infer entailment
    label = "entailment"

print(label)