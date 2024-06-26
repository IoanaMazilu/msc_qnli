sandy_age_premise = 30
sandy_age_hypothesis = 30

# the hypothesis refers to the age of Sandy mentioned in the premise
if sandy_age_hypothesis!= sandy_age_premise:
    # check if the hypothesis value contradicts the age of Sandy in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the age of Sandy
    # any age of Sandy greater than'sandy_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)