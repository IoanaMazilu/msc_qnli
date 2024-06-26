 socks_premise = 10
socks_hypothesis = 40

# the hypothesis refers to the number of socks John has, as mentioned in the premise
if socks_premise >= socks_hypothesis:
    # check if the number of socks in the premise contradicts the hypothesis
    label = "contradiction"
elif socks_premise < socks_hypothesis:
    # if the number of socks in the premise is less than the number in the hypothesis, we can infer entailment
    label = "entailment"
else:
    # if the number of socks in the premise is equal to the number in the hypothesis, we can infer neutral
    label = "neutral"

print(label)
