discount_premise = 16
discount_hypothesis = 16

# the hypothesis talks about the discount on the cupboard's price, referenced also in the premise
if discount_hypothesis < discount_premise:
    # check if the discount in the hypothesis contradicts the discount in the premise
    label = "contradiction"
elif discount_hypothesis > discount_premise:
    # check if the discount in the hypothesis contradicts the discount in the premise
    label = "contradiction"
else:
    # the premise gives the exact discount, which is also mentioned in the hypothesis
    label = "entailment"

print(label)
