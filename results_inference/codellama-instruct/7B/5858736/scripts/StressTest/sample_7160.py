age_sandy_premise = 6
age_sandy_hypothesis = 4

# the hypothesis talks about the age of Sandy after 4 years, referenced also in the premise
if age_sandy_hypothesis <= age_sandy_premise:
    # check if the hypothesis value contradicts the estimate of 38 years
    label = "contradiction"
else:
    # the premise gives only an estimate for Sandy's age
    # any number of years greater than 38 years is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
