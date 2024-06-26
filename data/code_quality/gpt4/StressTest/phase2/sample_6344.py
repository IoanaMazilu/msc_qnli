discount_premise = 288
discount_hypothesis = 888

# the hypothesis refers to the same discount amount mentioned in the premise
if discount_premise != discount_hypothesis:
    # if the discount amount in the hypothesis contradicts the discount amount in the premise
    label = "contradiction"
else:
    # if the discount amount in the hypothesis does not contradict the discount amount in the premise
    label = "entailment"

print(label)
