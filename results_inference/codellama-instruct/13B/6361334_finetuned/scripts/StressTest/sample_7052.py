total_shares_premise = 1300
total_shares_hypothesis = 1300
deepak_share_premise = 1300
deepak_share_hypothesis = 1300

# the hypothesis refers to the total number of shares and the share of Deepak, both mentioned in the premise
if total_shares_hypothesis < total_shares_premise:
    # check if the hypothesis value contradicts the total number of shares in the premise
    label = "contradiction"
elif deepak_share_hypothesis > deepak_share_premise:
    # check if the hypothesis value contradicts the share of Deepak in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
