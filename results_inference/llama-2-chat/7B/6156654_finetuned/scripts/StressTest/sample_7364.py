discount_premise = 30
discount_hypothesis = 30

# the hypothesis talks about the discount on the listed price, which is also mentioned in the premise
if discount_hypothesis <= discount_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif discount_hypothesis > discount_premise:
    # check if the hypothesis value is greater than the premise value
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise value, we can infer entailment
    label = "entailment"

print(label)
