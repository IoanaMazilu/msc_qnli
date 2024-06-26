john_ratio_premise = 3800
john_ratio_hypothesis = 4800
jose_ratio_premise = 3800
jose_ratio_hypothesis = 4800
binoy_ratio_premise = 3800
binoy_ratio_hypothesis = 4800

# the hypothesis talks about the number of people in a ratio, referenced also in the premise
if john_ratio_hypothesis <= john_ratio_premise:
    # check if the hypothesis value contradicts the estimate of more than 'john_ratio_premise'
    label = "contradiction"
elif jose_ratio_hypothesis <= jose_ratio_premise:
    # check if the hypothesis value contradicts the estimate of more than 'jose_ratio_premise'
    label = "contradiction"
elif binoy_ratio_hypothesis <= binoy_ratio_premise:
    # check if the hypothesis value contradicts the estimate of more than 'binoy_ratio_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
