rent_paid_premise = 58
rent_paid_hypothesis = 38

# the hypothesis refers to the amount Dhoni paid for renting a tool, also mentioned in the premise
if rent_paid_hypothesis >= rent_paid_premise:
    # check if the hypothesis value contradicts the estimate of less than 'rent_paid_premise'
    label = "contradiction"
elif rent_paid_hypothesis < rent_paid_premise:
    # the premise gives only an estimate for the rent paid
    # any amount less than 'rent_paid_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
