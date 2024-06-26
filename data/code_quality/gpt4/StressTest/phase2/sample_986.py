socks_pairs_premise = 12
socks_pairs_hypothesis = 42

# the hypothesis talks about the number of Angela's matched sock pairs, referenced also in the premise
if socks_pairs_hypothesis != socks_pairs_premise:
    # check if the hypothesis value contradicts the number of sock pairs in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the number of sock pairs in the premise, we can infer entailment
    label = "entailment"

print(label)
