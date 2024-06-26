distance_premise = 20
walking_speed_premise = 4
running_speed_premise = 6

distance_hypothesis = 80
walking_speed_hypothesis = 4
running_speed_hypothesis = 6

# the hypothesis talks about the distance traveled by Brad, referenced also in the premise
if distance_hypothesis <= distance_premise:
    # check if the hypothesis value contradicts the estimate of less than 'distance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance traveled by Brad
    # any distance traveled by Brad greater than or equal to 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
