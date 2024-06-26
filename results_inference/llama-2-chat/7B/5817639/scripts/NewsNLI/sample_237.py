injured_premise = 50
injured_hypothesis = 50

# the hypothesis mentions the same number of injured people as the premise
if injured_hypothesis == injured_premise:
    # if the hypothesis and premise values are the same, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis and premise values are different, we can infer contradiction or neutrality
    if injured_hypothesis < injured_premise:
        label = "contradiction"
    else:
        label = "neutral"

print(label)
