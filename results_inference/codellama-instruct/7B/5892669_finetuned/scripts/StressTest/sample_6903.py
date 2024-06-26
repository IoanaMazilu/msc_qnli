rent_paid_premise = 160
rent_paid_hypothesis = 360

# the hypothesis refers to the amount Rahul paid for renting the tool, which is also mentioned in the premise
if rent_paid_hypothesis <= rent_paid_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
