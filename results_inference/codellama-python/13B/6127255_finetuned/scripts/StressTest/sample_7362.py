discount_premise = 30
discount_hypothesis = 10

# the hypothesis refers to the discount percentage on the calculator's listed price mentioned in the premise
if discount_premise < discount_hypothesis:
    # check if the discount in the premise contradicts the discount estimate in the hypothesis
    label = "contradiction"
elif discount_premise == discount_hypothesis:
    # check if the discount in the premise is equal to the discount estimate in the hypothesis
    label = "entailment"
else:
    # if the discount in the premise is greater than the discount estimate in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
