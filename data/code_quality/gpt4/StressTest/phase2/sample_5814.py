socks_premise = 11
socks_hypothesis = 81

# the hypothesis compares the number of matched socks Angela has with the number mentioned in the premise
if socks_premise >= socks_hypothesis:
    # check if the number of socks in the premise contradicts the hypothesis that Angela has less than 'socks_hypothesis'
    label = "contradiction"
elif socks_premise == socks_hypothesis - 1:
    # check if the number of socks in the premise can be directly inferred from the hypothesis
    label = "entailment"
else:
    # the number of socks in the premise is consistent with the hypothesis, but cannot be directly inferred from it
    label = "neutral"

print(label)
