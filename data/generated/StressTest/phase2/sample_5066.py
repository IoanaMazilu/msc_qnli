# Premise: Vijay sells a cupboard at 14% below cost price.
# Hypothesis: Vijay sells a cupboard at less than 14% below cost price.
# Golden Label: contradiction

discount_premise = 14
discount_hypothesis = 14

# the hypothesis refers to the discount percentage on the cupboard's cost price mentioned in the premise
if discount_hypothesis >= discount_premise:
    # check if the hypothesis value contradicts the premise estimate of 'discount_premise'
    label = "contradiction"
else:
    # any discount less than 'discount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

