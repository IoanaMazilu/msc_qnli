discount_premise = 288
discount_hypothesis = 588

# the hypothesis refers to the discount amount mentioned in the premise
if discount_premise >= discount_hypothesis:
    # check if the estimate of 'discount_hypothesis' contradicts the discount amount in the premise
    label = "contradiction"
elif discount_premise < discount_hypothesis:
    # if the discount amount in the hypothesis is less than the premise, we can infer entailment
    label = "entailment"

print(label)
