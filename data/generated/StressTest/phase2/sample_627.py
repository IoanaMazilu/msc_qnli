# Premise: John has 10 pairs of matched socks.
# Hypothesis: John has less than 70 pairs of matched socks.
# Golden Label: entailment

socks_premise = 10
socks_hypothesis = 70

# the hypothesis refers to the number of socks John has, which is also mentioned in the premise
if socks_hypothesis <= socks_premise:
    # check if the hypothesis estimate contradicts the number of John's socks mentioned in the premise
    label = "contradiction"
elif socks_premise >= socks_hypothesis:
    # check if the number of John's socks in the premise contradicts the estimate of 'socks_hypothesis'
    label = "contradiction"
else:
    # the number of socks John has according to the premise is less than the upper limit given in the hypothesis
    # thus, the hypothesis does not contradict the premise, but it is not explicitly entailed by the premise either
    label = "neutral"

print(label)

