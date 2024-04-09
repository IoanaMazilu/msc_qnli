premise_age = 38
hypothesis_age = 38
premise_years = 4
hypothesis_years = 6

# the hypothesis talks about the age of Sandy after a certain number of years
if hypothesis_age == premise_age:
    # check if the hypothesis value contradicts the estimate of 'premise_age'
    label = "contradiction"
elif hypothesis_years > premise_years:
    # check if the number of years in the hypothesis contradicts the number of years reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the age of Sandy after a certain number of years
    # any age consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
