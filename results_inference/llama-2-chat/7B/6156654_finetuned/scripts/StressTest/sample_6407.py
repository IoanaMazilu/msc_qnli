matched_socks_premise = 15
matched_socks_hypothesis = 75

# the hypothesis refers to the number of matched socks Angela has, which is also mentioned in the premise
if matched_socks_hypothesis!= matched_socks_premise:
    # check if the number of matched socks in the hypothesis contradicts the number of matched socks in the premise
    label = "contradiction"
else:
    # if the number of matched socks in the hypothesis is the same as in the premise, we can infer entailment
    label = "entailment"

print(label)
