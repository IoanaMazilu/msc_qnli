miami_to_kennedy_ratio_premise = 1/4
miami_to_kennedy_ratio_hypothesis = 6/4
miami_to_logan_ratio_premise = 3
miami_to_logan_ratio_hypothesis = 3

# the hypothesis refers to the same ratios as the premise
if miami_to_kennedy_ratio_hypothesis != miami_to_kennedy_ratio_premise:
    # check if the hypothesis' Miami to Kennedy airport ratio contradicts the premise's ratio
    label = "contradiction"
elif miami_to_logan_ratio_hypothesis != miami_to_logan_ratio_premise:
    # check if the hypothesis' Miami to Logan airport ratio contradicts the premise's ratio
    label = "contradiction"
else:
    # if the hypothesis' ratios do not contradict the premise's ratios, we can infer entailment
    label = "entailment"

print(label)
