john_share_premise = 2600
john_share_hypothesis = 6600
jose_share_premise = 2600
jose_share_hypothesis = 6600
binoy_share_premise = 2600
binoy_share_hypothesis = 6600

# the hypothesis refers to the number of shares of John, Jose, and Binoy in the ration 2:4:6
if john_share_hypothesis <= john_share_premise:
    # check if the estimate of 'john_share_hypothesis' contradicts the number of John's shares in the premise
    label = "contradiction"
elif jose_share_hypothesis!= jose_share_premise:
    # check if the number of Jose's shares in the hypothesis contradicts the number of Jose's shares reported in the premise
    label = "contradiction"
elif binoy_share_hypothesis!= binoy_share_premise:
    # check if the number of Binoy's shares in the hypothesis contradicts the number of Binoy's shares reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
