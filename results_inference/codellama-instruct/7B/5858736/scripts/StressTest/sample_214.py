premise_avg_speed = 76
hypothesis_avg_speed = 36

# the hypothesis talks about the average speed of the whole journey, referenced also in the premise
if hypothesis_avg_speed <= premise_avg_speed:
    # check if the hypothesis value contradicts the estimate of less than 'premise_avg_speed'
    label = "contradiction"
else:
    # the premise gives only an estimate for the average speed of the whole journey
    # any number of mph greater than 'premise_avg_speed' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
