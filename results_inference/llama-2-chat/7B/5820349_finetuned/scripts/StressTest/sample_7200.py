socks_premise = 13
socks_hypothesis = 83

# the hypothesis refers to the number of sock pairs Angela has, mentioned in the premise
if socks_premise >= socks_hypothesis:
    # check if the number of sock pairs in the premise contradicts the estimate of less than'socks_hypothesis'
    label = "contradiction"
else:
    # if the number of sock pairs in the premise does not contradict the estimate in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
