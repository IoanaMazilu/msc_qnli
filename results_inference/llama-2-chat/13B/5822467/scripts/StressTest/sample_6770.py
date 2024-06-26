john_share_premise = 2 * 6600 // 3
john_share_hypothesis = 2 * (less than 6600) // 3

jose_share_premise = 4 * 6600 // 3
jose_share_hypothesis = 4 * (less than 6600) // 3

binoy_share_premise = 6 * 6600 // 3
binoy_share_hypothesis = 6 * (less than 6600) // 3

# compare the shares of each person in the premise and hypothesis
if john_share_premise <= john_share_hypothesis:
    # check if the estimate of 'john_share_hypothesis' contradicts the share of John in the premise
    label = "contradiction"
elif jose_share_hypothesis!= jose_share_premise:
    # check if the share of Jose in the hypothesis contradicts the share of Jose reported in the premise
    label = "contradiction"
elif binoy_share_hypothesis!= binoy_share_premise:
    # check if the share of Binoy in the hypothesis contradicts the share of Binoy reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
