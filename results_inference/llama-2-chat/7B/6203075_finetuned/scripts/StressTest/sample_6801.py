denominations_premise = 50 or 100
denominations_hypothesis = 70 or 100

# the hypothesis refers to the denominations of bonds that Robert purchased, which is also mentioned in the premise
if denominations_hypothesis!= denominations_premise:
    # check if the denominations in the hypothesis contradict the denominations in the premise
    label = "contradiction"
else:
    # if the denominations in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
