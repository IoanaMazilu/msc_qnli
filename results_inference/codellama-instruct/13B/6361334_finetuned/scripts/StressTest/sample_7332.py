percentage_samsung_premise = 75
percentage_iphone_premise = 70
percentage_samsung_hypothesis = 85

# the hypothesis refers to the percentage of users using Samsung and iPhone phones in the same company
# the premise mentions the percentage of users using Samsung and iPhone phones in the same company
if percentage_samsung_hypothesis <= percentage_samsung_premise:
    # check if the hypothesis value contradicts the estimate of more than 'percentage_samsung_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of users using Samsung phones
    # any percentage of users using Samsung phones greater than 'percentage_samsung_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
