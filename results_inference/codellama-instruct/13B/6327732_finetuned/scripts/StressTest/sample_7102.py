miles_premise = 340
miles_hypothesis = 240
speed_premise = 60
speed_hypothesis = 60

# the hypothesis refers to the total number of miles driven and the speed at which they were driven
if miles_hypothesis!= miles_premise:
    # check if the total number of miles driven in the hypothesis contradicts the total number of miles driven in the premise
    label = "contradiction"
elif speed_hypothesis!= speed_premise:
    # check if the speed at which the miles were driven in the hypothesis contradicts the speed at which the miles were driven in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
