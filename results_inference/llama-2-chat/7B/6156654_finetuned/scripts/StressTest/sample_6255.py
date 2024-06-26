discount_premise = 20
discount_hypothesis = 30

# The hypothesis refers to the discount negotiated by Saren, which is also mentioned in the premise
if discount_premise >= discount_hypothesis:
    # If the discount in the premise is greater than or equal to the discount in the hypothesis, we can infer entailment
    label = "entailment"
elif discount_premise < discount_hypothesis:
    # If the discount in the premise is less than the discount in the hypothesis, we can infer contradiction
    label = "contradiction"
else:
    # If the discount in the premise is equal to the discount in the hypothesis, we can infer neutral
    label = "neutral"

print(label)
