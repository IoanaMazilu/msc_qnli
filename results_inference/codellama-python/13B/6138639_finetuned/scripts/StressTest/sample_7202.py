pairs_socks_premise = 13
pairs_socks_hypothesis = 83

# the hypothesis talks about the number of pairs of socks Angela has, referenced also in the premise
if pairs_socks_hypothesis!= pairs_socks_premise:
    # check if the number of pairs of socks in the hypothesis contradicts the number of pairs of socks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
