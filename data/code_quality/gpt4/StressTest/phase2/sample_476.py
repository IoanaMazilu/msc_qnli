ashok_share_premise = 1/9
ashok_share_hypothesis = ashok_share_premise 

# the hypothesis refers to the share of Ashok's capital investment in a business relative to Pyarelal's, which is mentioned in the premise
if ashok_share_hypothesis < ashok_share_premise:
    # check if the hypothesis value contradicts the share of capital investment of Ashok in the premise
    label = "contradiction"
elif ashok_share_hypothesis > ashok_share_premise:
    # check if the hypothesis value contradicts the share of capital investment of Ashok in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)