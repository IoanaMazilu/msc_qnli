x_per_hour_premise = 0
x_per_hour_hypothesis = 0

# the hypothesis talks about the hourly pay of Harry, referenced also in the premise
if x_per_hour_hypothesis <= x_per_hour_premise:
    # check if the hypothesis value contradicts the estimate of 'x_per_hour_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the hourly pay
    # any hourly pay greater than 'x_per_hour_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
