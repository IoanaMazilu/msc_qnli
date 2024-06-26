billion_premise = 1000000000
billion_hypothesis = 1000000000
trillion_premise = 1000000000000
trillion_hypothesis = 1000000000000

# the hypothesis mentions the same values as the premise, so we can infer entailment
if billion_hypothesis == billion_premise and trillion_hypothesis == trillion_premise:
    label = "entailment"
else:
    label = "contradiction"

print(label)
