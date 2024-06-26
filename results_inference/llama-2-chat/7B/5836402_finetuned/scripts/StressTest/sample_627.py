socks_premise = 10
socks_hypothesis = 70

# the hypothesis refers to the number of socks John has, which is also mentioned in the premise
if socks_premise >= socks_hypothesis:
    # check if the premise value contradicts the estimate of'socks_hypothesis'
    label = "contradiction"
elif socks_premise < socks_hypothesis:
    # if the number of socks in the premise is less than the estimate in the hypothesis, we can infer entailment
    label = "entailment"
else:
    # if the premise value is equal to the estimate in the hypothesis, we cannot infer entailment or contradiction
    label = "neutral"

print(label)
