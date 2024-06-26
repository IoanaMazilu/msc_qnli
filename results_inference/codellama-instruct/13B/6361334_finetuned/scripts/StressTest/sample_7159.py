sandy_age_premise = 4
sandy_age_hypothesis = 6

# the hypothesis refers to the number of years after which Sandy's age will be 38 years
if sandy_age_hypothesis <= sandy_age_premise:
    # check if the hypothesis value contradicts the estimate of more than'sandy_age_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years
    # any number of years greater than'sandy_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
