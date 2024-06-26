rent_paid_premise = 360
rent_paid_hypothesis = 160

# the hypothesis refers to the amount of rent paid by Rahul, which is also mentioned in the premise
if rent_paid_hypothesis >= rent_paid_premise:
    # check if the amount of rent in the hypothesis contradicts the estimate of less than'rent_paid_premise'
    label = "contradiction"
elif rent_paid_hypothesis < rent_paid_premise:
    # the premise gives only an estimate for the rent
    # any amount of rent less than'rent_paid_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)