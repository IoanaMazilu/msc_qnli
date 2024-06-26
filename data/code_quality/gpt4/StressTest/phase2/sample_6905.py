rent_paid_premise = 160
rent_paid_hypothesis = 760

# the hypothesis refers to the amount paid to rent the tool mentioned in the premise
if rent_paid_hypothesis != rent_paid_premise:
    # check if the amount paid in the hypothesis contradicts the amount paid reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
