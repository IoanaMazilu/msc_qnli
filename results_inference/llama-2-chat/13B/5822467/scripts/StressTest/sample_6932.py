premise_age = 30
hypothesis_age = 30
years_premise = 6

# the hypothesis talks about the age of Sandy after less than 6 years
if hypothesis_age <= years_premise:
    # check if the hypothesis value contradicts the estimate of 'years_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the age of Sandy after 6 years
    # any age less than or equal to 30 years is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
