payback_years_premise = 50
payback_years_hypothesis = 40

# the hypothesis talks about the number of years to pay back a loan which is also mentioned in the premise
if payback_years_hypothesis > payback_years_premise:
    # check if the number of years in the hypothesis contradicts the maximum number of years specified in the premise
    label = "contradiction"
else:
    # the premise gives a maximum number of years to pay back the loan
    # any number of years less than or equal to 'payback_years_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
