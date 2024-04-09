socks_premise = 13
socks_hypothesis = 83

# the hypothesis refers to the number of Angela's matched socks mentioned in the premise
if socks_premise >= socks_hypothesis:
    # check if the number of socks in the premise contradicts the hypothesis estimate of less than'socks_hypothesis'
    label = "contradiction"
else:
    # if the premise number of socks does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
