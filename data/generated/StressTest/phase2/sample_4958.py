# Premise: Vijay sells a cupboard at 16% below cost price.
# Hypothesis: Vijay sells a cupboard at 56% below cost price.
# Golden Label: contradiction

discount_premise = 16
discount_hypothesis = 56

# the hypothesis talks about the selling price of a cupboard, which is also referenced in the premise
if discount_hypothesis < discount_premise:
    # check if the discount in the hypothesis contradicts the discount in the premise
    label = "contradiction"
elif discount_hypothesis == discount_premise:
    # check if the discount in the hypothesis is fully and explicitly entailed from the premise
    label = "entailment"
else:
    # the premise gives a specific discount for the cupboard
    # any discount greater than 'discount_premise' is inconsistent with the premise, but cannot be explicitly contradicted either
    label = "neutral"

print(label)

