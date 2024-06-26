sandy_age_premise = 6
sandy_age_hypothesis = 30

# the hypothesis refers to the number of years after which Sandy's age will be 30 years
if sandy_age_hypothesis <= sandy_age_premise:
    # check if the estimate of'sandy_age_hypothesis' contradicts the number of years in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years
    # any number of years greater than'sandy_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
