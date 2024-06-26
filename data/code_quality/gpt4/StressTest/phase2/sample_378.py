discount_premise = 20
discount_hypothesis = 50

# the hypothesis refers to the discount on the original price of an item mentioned in the premise
if discount_premise >= discount_hypothesis:
    # check if the discount in the premise contradicts the hypothesis of "less than 50%"
    label = "contradiction"
else:
    # if the discount in the premise is less than the discount in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
