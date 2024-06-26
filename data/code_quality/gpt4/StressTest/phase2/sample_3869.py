sock_pairs_premise = 14
sock_pairs_hypothesis = 74

# the hypothesis talks about the number of Angela's matched sock pairs, referenced also in the premise
if sock_pairs_hypothesis != sock_pairs_premise:
    # check if the number of sock pairs in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the number of sock pairs in the hypothesis matches the number reported in the premise, we can infer entailment
    label = "entailment"

print(label)
