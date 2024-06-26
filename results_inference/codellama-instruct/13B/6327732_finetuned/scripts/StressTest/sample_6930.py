sandy_age_premise = 6
sandy_age_hypothesis = 30

# the hypothesis refers to the age of Sandy after a certain number of years
if sandy_age_hypothesis <= sandy_age_premise:
    # check if the estimate of'sandy_age_hypothesis' contradicts the age of Sandy in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the age of Sandy
    # any age greater than'sandy_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
