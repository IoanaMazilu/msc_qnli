jack_time_premise = 5
lee_time_premise = 10
jack_time_hypothesis = 6
lee_time_hypothesis = 10

# the hypothesis refers to the time Jack and Lee take to finish each lap, as mentioned in the premise
if jack_time_hypothesis <= jack_time_premise:
    # check if the hypothesis value for Jack contradicts the estimate of more than 'jack_time_premise'
    label = "contradiction"
elif lee_time_hypothesis!= lee_time_premise:
    # check if the hypothesis value for Lee contradicts the exact time mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only estimates for the time Jack and Lee take to finish each lap
    # any time greater than 'jack_time_premise' for Jack and 'lee_time_premise' for Lee is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
