arrival_time_premise = 60
arrival_time_hypothesis = 30

# the hypothesis refers to the arrival time of Alice in City A, also mentioned in the premise
if arrival_time_hypothesis >= arrival_time_premise:
    # check if the arrival time in the hypothesis contradicts the arrival time estimate in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the arrival time
    # any arrival time less than 'arrival_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
