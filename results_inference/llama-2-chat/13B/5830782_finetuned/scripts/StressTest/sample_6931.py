years_future_premise = 2
years_future_hypothesis = 6
age_future_premise = 30
age_future_hypothesis = 30

# the hypothesis talks about the number of years in the future and the age at that time, referenced also in the premise
if years_future_hypothesis <= years_future_premise:
    # check if the hypothesis value contradicts the estimate of more than 'years_future_premise'
    label = "contradiction"
elif age_future_hypothesis!= age_future_premise:
    # check if the future age in the hypothesis contradicts the future age reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years in the future
    # any number of years greater than 'years_future_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
