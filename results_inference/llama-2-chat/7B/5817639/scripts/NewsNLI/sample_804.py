bombs_premise = 2
bombs_hypothesis = 2

# the hypothesis mentions the same number of bombs as the premise
if bombs_hypothesis == bombs_premise:
    # if the hypothesis and premise match, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis and premise do not match, we can infer contradiction or neutrality
    pass

print(label)
