pairs_socks_premise = 10
pairs_socks_hypothesis = 20

# the hypothesis talks about the number of pairs of socks John has, referenced also in the premise
if pairs_socks_hypothesis!= pairs_socks_premise:
    # check if the number of pairs of socks in the hypothesis contradicts the number of pairs of socks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
