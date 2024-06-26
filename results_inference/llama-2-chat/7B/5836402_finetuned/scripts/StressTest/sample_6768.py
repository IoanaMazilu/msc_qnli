total_ration_premise = 6600
john_ratio_premise = 2/6
jose_ratio_premise = 4/6
binoy_ratio_premise = 6/6

john_ratio_hypothesis = 2/6
jose_ratio_hypothesis = 4/6
binoy_ratio_hypothesis = 6/6

# the hypothesis refers to the ratio of John, Jose and Binoy in the premise
if total_ration_premise <= total_ration_hypothesis:
    # check if the estimate of 'total_ration_hypothesis' contradicts the total ratio in the premise
    label = "contradiction"
elif john_ratio_hypothesis!= john_ratio_premise or jose_ratio_hypothesis!= jose_ratio_premise or binoy_ratio_hypothesis!= binoy_ratio_premise:
    # check if the ratios in the hypothesis contradict the ratios reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
