# Premise: After more than 5 years, Arun's age will be 19 years.
# Hypothesis: After 7 years, Arun's age will be 19 years.
# Golden Label: neutral

arun_future_age_premise = 19
arun_future_age_hypothesis = 19
time_pass_premise = 5
time_pass_hypothesis = 7

# the hypothesis talks about Arun's future age and the number of years to pass, which is also mentioned in the premise
if arun_future_age_hypothesis != arun_future_age_premise:
    # check if the future age of Arun in the hypothesis contradicts the future age of Arun in the premise
    label = "contradiction"
elif time_pass_hypothesis <= time_pass_premise:
    # check if the number of years to pass in the hypothesis contradicts the estimate of more than 'time_pass_premise'
    label = "contradiction"
else:
    # the premise only gives an estimate for the number of years to pass
    # any number of years greater than 'time_pass_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

