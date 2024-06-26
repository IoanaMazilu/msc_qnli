arun_age_future_premise = 40
arun_age_future_hypothesis = 40
years_future_premise = 5
years_future_hypothesis = 2

# the hypothesis talks about Arun's age in the future, mentioned also in the premise
if arun_age_future_hypothesis != arun_age_future_premise:
    # check if Arun's future age in the hypothesis contradicts Arun's future age in the premise
    label = "contradiction"
elif years_future_hypothesis >= years_future_premise:
    # check if the number of years in the future in the hypothesis contradicts the number of years in the future mentioned in the premise
    label = "contradiction"
else:
    # the premise gives a specific number of years in the future for Arun's age
    # any number of years less than 'years_future_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
