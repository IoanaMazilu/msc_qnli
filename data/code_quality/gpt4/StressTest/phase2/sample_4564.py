max_hours_premise = 60
max_hours_hypothesis = 50

# the hypothesis talks about the maximum number of hours Mary works, referenced also in the premise
if max_hours_hypothesis >= max_hours_premise:
    # check if the hypothesis value contradicts the estimate of less than 'max_hours_premise'
    label = "contradiction"
elif max_hours_hypothesis < max_hours_premise:
    # the premise gives only an estimate for the maximum number of hours Mary works
    # a number of maximum hours less than 'max_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
