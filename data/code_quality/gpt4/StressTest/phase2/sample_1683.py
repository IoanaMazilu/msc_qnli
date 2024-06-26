future_age_multiplier_premise = 4
future_age_years_premise = 18
past_age_years_premise = 18

future_age_years_hypothesis = 38
future_age_multiplier_hypothesis = 4
past_age_years_hypothesis = 18

# the hypothesis refers to the same time periods and age multiplier as in the premise
if future_age_multiplier_premise != future_age_multiplier_hypothesis or past_age_years_premise != past_age_years_hypothesis:
    # check if the age multiplier or the past age years in the hypothesis contradict those in the premise
    label = "contradiction"
elif future_age_years_hypothesis <= future_age_years_premise:
    # check if the future age years in the hypothesis contradict the future age years in the premise
    label = "contradiction"
else:
    # the premise gives a specific future age year
    # any future age year greater than 'future_age_years_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
