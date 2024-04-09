rent_paid_premise = 160
rent_paid_hypothesis = 360

# the hypothesis refers to the amount Rahul paid to rent the tool, mentioned in the premise
if rent_paid_premise >= rent_paid_hypothesis:
    # check if the estimate of'rent_paid_hypothesis' contradicts the amount Rahul paid in the premise
    label = "contradiction"
elif rent_paid_premise < rent_paid_hypothesis:
    # if the amount Rahul paid in the premise is less than'rent_paid_hypothesis', we can infer entailment
    label = "entailment"

print(label)
