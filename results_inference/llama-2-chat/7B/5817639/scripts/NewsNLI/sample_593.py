injured_premise = 2
injured_hypothesis = 2

# check if the number of people injured in the hypothesis matches the number of people injured in the premise
if injured_hypothesis == injured_premise:
    # if the hypothesis and premise match, we can infer entailment
    label = "entailment"
elif injured_hypothesis < injured_premise:
    # if the number of people injured in the hypothesis is less than the number of people injured in the premise, we can infer contradiction
    label = "contradiction"
else:
    # if the hypothesis and premise do not match, we cannot infer entailment or contradiction
    label = "neutral"

print(label)
