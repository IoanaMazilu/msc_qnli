matched_socks_premise = 10
matched_socks_hypothesis = 40

# the hypothesis refers to the number of matched socks John has, which is also mentioned in the premise
if matched_socks_premise >= matched_socks_hypothesis:
    # check if the number of matched socks in the premise contradicts the estimate of less than'matched_socks_hypothesis'
    label = "contradiction"
else:
    # if the number of matched socks in the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)