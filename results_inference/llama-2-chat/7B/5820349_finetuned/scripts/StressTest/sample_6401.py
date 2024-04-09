miami_kennedy_ratio_premise = 1/2
miami_kennedy_ratio_hypothesis = 3/2
logan_ratio_premise = 4
logan_ratio_hypothesis = 4

# the hypothesis refers to the ratio of passengers using Miami, Kennedy, and Logan airports, as mentioned in the premise
if miami_kennedy_ratio_hypothesis!= miami_kennedy_ratio_premise:
    # check if the ratio of passengers using Miami and Kennedy airports in the hypothesis contradicts the ratio reported in the premise
    label = "contradiction"
elif logan_ratio_hypothesis!= logan_ratio_premise:
    # check if the ratio of passengers using Logan Airport in the hypothesis contradicts the ratio reported in the premise
    label = "contradiction"
else:
    # if the hypothesis ratios do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
