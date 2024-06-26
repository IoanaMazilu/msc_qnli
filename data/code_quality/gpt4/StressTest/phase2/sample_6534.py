miami_kennedy_ratio_premise = 1/3
miami_kennedy_ratio_hypothesis = 7/3
miami_logan_ratio_premise = 4
miami_logan_ratio_hypothesis = 4

# the hypothesis refers to the same ratios between the airports' usage described in the premise
if miami_kennedy_ratio_premise != miami_kennedy_ratio_hypothesis:
    # check if the ratio between Miami and Kennedy airports' usage in the hypothesis contradicts the one given in the premise
    label = "contradiction"
elif miami_logan_ratio_premise != miami_logan_ratio_hypothesis:
    # check if the ratio between Miami and Logan airports' usage in the hypothesis contradicts the one given in the premise
    label = "contradiction"
else:
    # if the hypothesis values and ratios do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
