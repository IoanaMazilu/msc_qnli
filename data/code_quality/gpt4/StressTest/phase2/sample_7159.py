years_pass_premise = 4
sandy_age_future_premise = 38
years_pass_hypothesis = 6
sandy_age_future_hypothesis = 38

# the hypothesis talks about Sandy's age after a number of years, also mentioned in the premise
if sandy_age_future_hypothesis != sandy_age_future_premise or years_pass_hypothesis <= years_pass_premise:
    # check if the future age of Sandy in the hypothesis contradicts the age mentioned in the premise
    # or if the number of years passed in the hypothesis is less than or equal to the number in the premise
    label = "contradiction"
else:
    # the premise gives a minimum number of years for Sandy to reach 38
    # any number of years greater than 'years_pass_premise' is consistent with the premise, but can't be explicitly entailed from it
    label = "neutral"

print(label)
