age_future_premise = 88
age_future_hypothesis = 18
age_past_premise = 6
age_past_hypothesis = 6

# the hypothesis talks about Molly's age in the future and in the past, referenced also in the premise
if age_future_hypothesis >= age_future_premise:
    # check if the hypothesis value contradicts the estimate of less than 'age_future_premise'
    label = "contradiction"
elif age_past_hypothesis!= age_past_premise:
    # check if the age in the past in the hypothesis contradicts the age in the past reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the future age
    # any future age less than 'age_future_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
