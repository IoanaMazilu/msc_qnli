age_future_premise = 88
age_future_hypothesis = 18

# the hypothesis talks about Molly's age in the future, referenced also in the premise
if age_future_hypothesis >= age_future_premise:
    # check if the hypothesis value contradicts the estimate of less than 'age_future_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for Molly's future age
    # any age less than 'age_future_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
