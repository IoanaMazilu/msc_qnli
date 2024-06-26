rent_paid_premise = 360
rent_paid_hypothesis = 160

# the hypothesis refers to the amount Rahul paid for renting a tool, which is also mentioned in the premise
if rent_paid_hypothesis >= rent_paid_premise:
    # check if the hypothesis value contradicts the estimate of less than'rent_paid_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the rent paid
    # any rent paid less than'rent_paid_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
