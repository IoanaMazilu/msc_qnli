distance_premise = 80
distance_hypothesis = 20
walking_speed_premise = 4
walking_speed_hypothesis = 4
running_speed_premise = 6
running_speed_hypothesis = 6

# the hypothesis talks about the distance traveled by Brad, given specific values for Maxwell's walking and running speeds
if distance_hypothesis <= distance_premise:
    # check if the hypothesis value contradicts the estimate of less than 'distance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance traveled,
    # any distance traveled by Brad consistent with the premise is not entailment
    label = "neutral"

print(label)
