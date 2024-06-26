jack_time_premise = 5
lee_time_premise = 10
jack_time_hypothesis = 6
lee_time_hypothesis = 10

# the hypothesis talks about the time Jack and Lee take to finish each lap, which is also referenced in the premise
if jack_time_hypothesis <= jack_time_premise:
    # check if the time Jack takes in the hypothesis contradicts the premise
    label = "contradiction"
elif lee_time_hypothesis < lee_time_premise:
    # check if the time Lee takes in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the premise gives only a lower estimate for the time Jack and Lee take
    # the times given in the hypothesis are consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
