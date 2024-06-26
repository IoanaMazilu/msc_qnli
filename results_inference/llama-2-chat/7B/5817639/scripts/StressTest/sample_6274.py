lap_time_premise = 5
lap_time_hypothesis = 6

# the hypothesis talks about the time taken by Jack and Lee to finish each lap, referenced also in the premise
if lap_time_hypothesis <= lap_time_premise:
    # check if the hypothesis value contradicts the estimate of more than 'lap_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time taken by Jack and Lee to finish each lap
    # any time taken by Jack and Lee to finish each lap greater than 'lap_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
