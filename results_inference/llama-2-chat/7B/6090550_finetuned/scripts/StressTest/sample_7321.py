y_premise = 6
y_hypothesis = 3

# the hypothesis talks about the number of weeks Rikki went to the gym, referenced also in the premise
if y_hypothesis >= y_premise:
    # check if the hypothesis value contradicts the estimate of less than 'y_premise' weeks
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of weeks
    # any number of weeks less than 'y_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
