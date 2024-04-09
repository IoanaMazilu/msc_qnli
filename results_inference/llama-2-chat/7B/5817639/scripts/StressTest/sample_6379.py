x_per_hour_premise = 0 # initialize variable for premise
x_per_hour_hypothesis = 0 # initialize variable for hypothesis

# the hypothesis talks about the pay rate for Harry, referenced also in the premise
if x_per_hour_hypothesis <= x_per_hour_premise:
    # check if the hypothesis value contradicts the estimate of 'x_per_hour_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the pay rate
    # any pay rate greater than 'x_per_hour_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
