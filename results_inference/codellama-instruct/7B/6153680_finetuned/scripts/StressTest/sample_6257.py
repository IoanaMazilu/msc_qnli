discount_premise = 20
discount_hypothesis = 50

# the hypothesis talks about a discount for the present, referenced also in the premise
if discount_hypothesis!= discount_premise:
    # check if the discount in the hypothesis contradicts the discount in the premise
    label = "contradiction"
else:
    # if the discounts are the same, we can infer entailment
    label = "entailment"

print(label)
