john_age_multiple = 3
past_years_premise = 5
past_years_hypothesis = 6

# the hypothesis refers to the age ratio between John and Tom and the time frame mentioned in the premise
if past_years_hypothesis <= past_years_premise:
    # check if the time frame in the hypothesis contradicts the time frame in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time frame
    # any time frame greater than 'past_years_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
