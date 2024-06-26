total_shares_premise = 1300
deepak_shares_premise = 1300
total_shares_hypothesis = 4300
deepak_shares_hypothesis = 1300

# the hypothesis refers to the number of shares and the share of Deepak, both mentioned in the premise
if deepak_shares_hypothesis > deepak_shares_premise:
    # check if the hypothesis value contradicts the number of shares in the premise
    label = "contradiction"
elif total_shares_hypothesis < total_shares_premise:
    # check if the hypothesis value contradicts the total number of shares in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
