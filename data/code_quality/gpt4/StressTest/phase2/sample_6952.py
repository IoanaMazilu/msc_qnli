arun_age_premise = 40
arun_years_future_premise = 2
arun_age_hypothesis = 40
arun_years_future_hypothesis = 5

# the hypothesis talks about Arun's age after a number of years, which is also referenced in the premise
if arun_years_future_hypothesis <= arun_years_future_premise:
    # check if the hypothesis value contradicts the estimate of more than 'arun_years_future_premise' years
    label = "contradiction"
elif arun_age_hypothesis != arun_age_premise:
    # check if the age of Arun in the hypothesis contradicts the age mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years after which Arun will be of 'arun_age_premise'
    # any number of years greater than 'arun_years_future_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
