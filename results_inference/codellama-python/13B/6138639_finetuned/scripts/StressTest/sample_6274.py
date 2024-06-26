jack_lap_time_premise = 5
jack_lap_time_hypothesis = 6
lee_lap_time_premise = 10
lee_lap_time_hypothesis = 10

# the hypothesis talks about the time Jack and Lee need to finish a lap, referenced also in the premise
if jack_lap_time_hypothesis <= jack_lap_time_premise:
    # check if the hypothesis value contradicts the estimate of more than 'jack_lap_time_premise'
    label = "contradiction"
elif lee_lap_time_hypothesis!= lee_lap_time_premise:
    # check if the time Lee needs to finish a lap in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time Jack and Lee need to finish a lap
    # any time less than 'jack_lap_time_premise' and equal to 'lee_lap_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
