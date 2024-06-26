miles_traveled_premise = 8
speed_premise = 40
stopped_time_premise = 11
miles_traveled_hypothesis = 6
speed_hypothesis = 40
stopped_time_hypothesis = 11

# the hypothesis refers to the same traveling, stopping and speeding parts as the premise
if miles_traveled_hypothesis!= miles_traveled_premise:
    # check if the miles traveled in the hypothesis contradicts the miles traveled in the premise
    label = "contradiction"
elif speed_hypothesis!= speed_premise:
    # check if the speed in the hypothesis contradicts the speed in the premise
    label = "contradiction"
elif stopped_time_hypothesis!= stopped_time_premise:
    # check if the stopped time in the hypothesis contradicts the stopped time in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
