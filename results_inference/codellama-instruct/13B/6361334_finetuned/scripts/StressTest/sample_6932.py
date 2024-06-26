sandy_age_premise = 30
sandy_age_hypothesis = 30

# the hypothesis refers to the age of Sandy after 6 years, which is also mentioned in the premise
if sandy_age_hypothesis!= sandy_age_premise:
    # check if the hypothesis value contradicts the age of Sandy in the premise
    label = "contradiction"
else:
    # the premise gives an explicit age for Sandy after 6 years
    # any age of Sandy that is less than 30 years is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
