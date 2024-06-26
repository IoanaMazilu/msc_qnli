discount_premise = 288
discount_hypothesis = 888

# the hypothesis refers to the same discount mentioned in the premise
if discount_hypothesis!= discount_premise:
    # check if the discount value in the hypothesis contradicts the discount value in the premise
    label = "contradiction"
else:
    # if the discount values in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
