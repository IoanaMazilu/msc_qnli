drive_time_premise = 1 * 60 = 60
drive_time_hypothesis = 3 * 60 = 180

# the hypothesis talks about the total drive time, which is also referred to in the premise
if drive_time_hypothesis <= drive_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'drive_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the total drive time
    # any total drive time greater than 'drive_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
