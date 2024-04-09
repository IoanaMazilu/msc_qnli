total_time_premise = 4
total_time_hypothesis = 3

# the hypothesis talks about the total time spent jogging and walking, referenced also in the premise
if total_time_hypothesis <= total_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'total_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the total time spent jogging and walking
    # any total time less than 'total_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
