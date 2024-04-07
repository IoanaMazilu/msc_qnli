# Premise: Deepa bought a calculator at 30% discount on the listed price.
# Hypothesis: Deepa bought a calculator at less than 30% discount on the listed price.
# Golden Label: contradiction

discount_premise = 30
discount_hypothesis = 30

# the hypothesis refers to the discount on the calculator mentioned in the premise
if discount_hypothesis < discount_premise:
    # check if the discount in the hypothesis contradicts the discount mentioned in the premise
    label = "contradiction"
elif discount_hypothesis > discount_premise:
    # check if the discount in the hypothesis contradicts the discount mentioned in the premise
    label = "contradiction"
else:
    # if the discount mentioned in the hypothesis is the same as in the premise, we can infer entailment
    label = "entailment"

print(label)

