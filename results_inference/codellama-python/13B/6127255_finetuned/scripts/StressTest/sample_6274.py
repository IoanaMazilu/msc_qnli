jack_time_premise = 5
jack_time_hypothesis = 6
lee_time_premise = 10
lee_time_hypothesis = 10

# the hypothesis talks about the time Jack and Lee take to finish each lap, referenced also in the premise
if jack_time_hypothesis <= jack_time_premise:
    # check if the hypothesis value contradicts the estimate of more than 'jack_time_premise'
    label = "contradiction"
elif lee_time_hypothesis!= lee_time_premise:
    # check if the time Lee takes to finish each lap in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time Jack takes to finish each lap
    # any time greater than 'jack_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
