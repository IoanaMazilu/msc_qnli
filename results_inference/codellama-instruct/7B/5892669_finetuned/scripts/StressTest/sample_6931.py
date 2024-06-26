sandy_age_future_premise = 30
sandy_age_future_hypothesis = 30
years_until_future_premise = 2
years_until_future_hypothesis = 6

# the hypothesis refers to the same future age of Sandy as the premise, but with a different time frame
if sandy_age_future_hypothesis!= sandy_age_future_premise:
    # check if the future age of Sandy in the hypothesis contradicts the future age of Sandy in the premise
    label = "contradiction"
elif years_until_future_hypothesis <= years_until_future_premise:
    # check if the time frame in the hypothesis contradicts the time frame in the premise
    label = "contradiction"
else:
    # the premise gives only a lower limit for the time frame until Sandy's future age
    # any time frame greater than 'years_until_future_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
