years_future_premise = 4
years_future_hypothesis = 6
age_future_premise = 38
age_future_hypothesis = 38

# the hypothesis refers to the number of years in the future and the age at that time, mentioned in the premise
if years_future_hypothesis <= years_future_premise:
    # check if the number of years in the future in the hypothesis contradicts the number of years in the premise
    label = "contradiction"
elif age_future_hypothesis!= age_future_premise:
    # check if the age in the future in the hypothesis contradicts the age in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years in the future
    # any number of years greater than 'years_future_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
