john_ratio_premise = 2600
john_ratio_hypothesis = 6600
jose_ratio_premise = 4
jose_ratio_hypothesis = 4
binoy_ratio_premise = 6
binoy_ratio_hypothesis = 6

# the hypothesis talks about the ratio of John, Jose, and Binoy
if john_ratio_hypothesis <= john_ratio_premise:
    # check if the hypothesis value contradicts the estimate of more than 'john_ratio_premise'
    label = "contradiction"
elif jose_ratio_hypothesis!= jose_ratio_premise:
    # check if the ratio of Jose in the hypothesis contradicts the ratio of Jose reported in the premise
    label = "contradiction"
elif binoy_ratio_hypothesis!= binoy_ratio_premise:
    # check if the ratio of Binoy in the hypothesis contradicts the ratio of Binoy reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
