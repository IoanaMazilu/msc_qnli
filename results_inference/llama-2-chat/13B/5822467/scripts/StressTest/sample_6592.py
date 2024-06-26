elevator_floors_premise = 51
elevator_floors_hypothesis = 71
rate_per_minute_premise = 93

# the hypothesis talks about the floor number and rate of the elevator, referenced also in the premise
if elevator_floors_hypothesis <= elevator_floors_premise:
    # check if the hypothesis value contradicts the estimate of more than 'elevator_floors_premise'
    label = "contradiction"
elif rate_per_minute_premise!= rate_per_minute_hypothesis:
    # check if the rate of the elevator in the hypothesis contradicts the rate reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the floor number and rate of the elevator
    # any floor number and rate consistent with the premise cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
