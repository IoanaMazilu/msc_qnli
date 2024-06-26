john_ratio_premise = 2/3800
john_ratio_hypothesis = 2/4800
jose_ratio_premise = 4/3800
jose_ratio_hypothesis = 4/4800
binoy_ratio_premise = 6/3800
binoy_ratio_hypothesis = 6/4800

# the hypothesis refers to the ratios of John, Jose, and Binoy mentioned in the premise
if john_ratio_hypothesis!= john_ratio_premise:
    # check if the ratio of John in the hypothesis contradicts the ratio of John in the premise
    label = "contradiction"
elif jose_ratio_hypothesis!= jose_ratio_premise:
    # check if the ratio of Jose in the hypothesis contradicts the ratio of Jose in the premise
    label = "contradiction"
elif binoy_ratio_hypothesis!= binoy_ratio_premise:
    # check if the ratio of Binoy in the hypothesis contradicts the ratio of Binoy in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
