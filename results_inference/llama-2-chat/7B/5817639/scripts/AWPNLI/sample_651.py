apples_premise = float(504.0)
apples_hypothesis = float(129.0)

# compare the number of apples in the premise and hypothesis
if apples_premise == apples_hypothesis:
    # if the number of apples in the hypothesis is equal to the number of apples in the premise, we can infer entailment
    label = "entailment"
elif apples_hypothesis > apples_premise:
    # if the number of apples in the hypothesis is greater than the number of apples in the premise, we can infer contradiction
    label = "contradiction"
else:
    # if the number of apples in the hypothesis is less than or equal to the number of apples in the premise, we cannot infer any relation
    label = "neutral"

print(label)
