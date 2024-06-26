matched_socks_premise = 10
matched_socks_hypothesis = 70

# the hypothesis refers to the number of pairs of matched socks John has, which is also mentioned in the premise
if matched_socks_premise >= matched_socks_hypothesis:
    # check if the number of matched socks in the premise contradicts the estimate of less than'matched_socks_hypothesis'
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
