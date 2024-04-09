diagnosis_premise = "leukemia"
diagnosis_hypothesis = "leukemia"

# the hypothesis mentions the same medical condition as the premise
if diagnosis_hypothesis == diagnosis_premise:
    # if the hypothesis and premise match, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis and premise do not match, we can infer contradiction or neutrality
    pass

print(label)
