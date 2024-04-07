# Premise: 288 and the true discount on the same sum for the same time is Rs.
# Hypothesis: 888 and the true discount on the same sum for the same time is Rs.
# Golden Label: contradiction

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

