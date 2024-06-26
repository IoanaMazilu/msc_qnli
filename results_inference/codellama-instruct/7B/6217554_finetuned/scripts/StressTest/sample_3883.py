jogging_walking_hours_premise = 4
jogging_walking_hours_hypothesis = 3

# the hypothesis talks about the total number of hours jogging and walking, referenced also in the premise
if jogging_walking_hours_hypothesis >= jogging_walking_hours_premise:
    # check if the hypothesis value contradicts the estimate of less than 'jogging_walking_hours_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the total number of hours jogging and walking
    # any number of hours less than 'jogging_walking_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
