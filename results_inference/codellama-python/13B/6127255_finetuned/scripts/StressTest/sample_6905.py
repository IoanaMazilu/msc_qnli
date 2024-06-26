rent_paid_premise = 160
rent_paid_hypothesis = 760

# the hypothesis refers to the amount of rent paid by Rahul, which is also mentioned in the premise
if rent_paid_hypothesis!= rent_paid_premise:
    # check if the amount of rent in the hypothesis contradicts the amount of rent reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
