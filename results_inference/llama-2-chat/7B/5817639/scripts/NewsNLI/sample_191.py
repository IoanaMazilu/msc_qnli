victims_premise = 4
victims_hypothesis = 4

# the hypothesis mentions the same number of shooting victims as the premise
if victims_hypothesis == victims_premise:
    # if the hypothesis and premise match, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis and premise do not match, we can infer contradiction or neutrality
    pass

print(label)
