pubs_premise = 57000
pubs_hypothesis = 57000

# the hypothesis mentions the same number of pubs as the premise
if pubs_hypothesis == pubs_premise:
    # if the hypothesis and premise values are the same, we can infer entailment
    label = "entailment"
elif pubs_hypothesis < pubs_premise:
    # if the hypothesis value is less than the premise value, we can infer contradiction
    label = "contradiction"
else:
    # if the hypothesis and premise values are not the same, but do not contradict, we can infer neutrality
    label = "neutral"

print(label)
