x_per_hour_premise = 10 # replace with the value of x per hour in the premise
x_per_hour_hypothesis = 12 # replace with the value of x per hour in the hypothesis

# the hypothesis talks about the rate of pay for hours worked, which is also mentioned in the premise
if x_per_hour_hypothesis <= x_per_hour_premise:
    # check if the hypothesis value contradicts the estimate of x per hour in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the rate of pay,
    # any rate of pay greater than x per hour in the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
