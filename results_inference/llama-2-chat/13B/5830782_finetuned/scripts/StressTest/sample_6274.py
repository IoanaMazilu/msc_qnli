jack_time_premise = 5
lee_time_premise = 10
jack_time_hypothesis = 6
lee_time_hypothesis = 10

# the hypothesis refers to the time taken by Jack and Lee to finish each lap, as mentioned in the premise
if jack_time_hypothesis <= jack_time_premise:
    # check if the time taken by Jack in the hypothesis contradicts the estimate of more than 'jack_time_premise'
    label = "contradiction"
elif lee_time_hypothesis!= lee_time_premise:
    # check if the time taken by Lee in the hypothesis contradicts the time taken by Lee reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time taken by Jack
    # any time greater than 'jack_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
