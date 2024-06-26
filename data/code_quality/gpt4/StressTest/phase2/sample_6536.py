miami_to_kennedy_ratio_premise = 1/3
miami_to_logan_ratio_premise = 4
miami_to_kennedy_ratio_hypothesis = 1/3
miami_to_logan_ratio_hypothesis = 4

# the hypothesis is referring to the ratios of passengers that used Miami Airport to Kennedy and Logan Airports mentioned in the premise
if miami_to_kennedy_ratio_hypothesis != miami_to_kennedy_ratio_premise:
    # check if the ratio of passengers using Miami Airport to Kennedy Airport in the hypothesis contradicts the one in the premise
    label = "contradiction"
elif miami_to_logan_ratio_hypothesis != miami_to_logan_ratio_premise:
    # check if the ratio of passengers using Miami Airport to Logan Airport in the hypothesis contradicts the one in the premise
    label = "contradiction"
else:
    # if the ratios in the hypothesis do not contradict the ones in the premise, we can infer entailment
    label = "entailment"

print(label)
