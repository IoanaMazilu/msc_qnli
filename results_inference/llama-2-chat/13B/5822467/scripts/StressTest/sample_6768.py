john_share_premise = 6600 / 3
john_share_hypothesis = 2600
jose_share_premise = 6600 / 2
jose_share_hypothesis = 2600
binoy_share_premise = 6600 / 3
binoy_share_hypothesis = 2600

# the hypothesis refers to the number of shares among John, Jose, and Binoy
if john_share_hypothesis <= john_share_premise:
    # check if the estimate of 'john_share_hypothesis' contradicts the number of shares reported in the premise
    label = "contradiction"
elif jose_share_hypothesis!= jose_share_premise:
    # check if the number of shares in the hypothesis contradicts the number of shares reported in the premise
    label = "contradiction"
elif binoy_share_hypothesis!= binoy_share_premise:
    # check if the number of shares in the hypothesis contradicts the number of shares reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
