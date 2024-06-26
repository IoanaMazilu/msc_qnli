rent_paid_premise = 625
rent_paid_hypothesis = 125

# the hypothesis refers to the rental cost mentioned in the premise
if rent_paid_hypothesis >= rent_paid_premise:
    # check if the cost in the hypothesis contradicts the cost in the premise
    label = "contradiction"
elif rent_paid_hypothesis < rent_paid_premise:
    # the premise only gives an upper limit for the rent
    # any amount less than 'rent_paid_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
