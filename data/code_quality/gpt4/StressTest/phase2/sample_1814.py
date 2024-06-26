ashok_share_premise = 1/9
ashok_share_hypothesis = 1/9

# the hypothesis refers to Ashok's share in the business, which is also mentioned in the premise
if ashok_share_hypothesis != ashok_share_premise:
    # check if the share of Ashok in the hypothesis contradicts his share reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
