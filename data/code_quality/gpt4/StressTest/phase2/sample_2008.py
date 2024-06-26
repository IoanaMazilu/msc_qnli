dig_days_premise = 84
dig_days_hypothesis = 24

# the hypothesis refers to the number of days Paul needs to dig a well, which is also mentioned in the premise
if dig_days_hypothesis >= dig_days_premise:
    # check if the hypothesis value contradicts the estimate of less than 'dig_days_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days
    # any number of days less than 'dig_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
