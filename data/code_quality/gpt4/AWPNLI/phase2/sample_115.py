distance_premise = 6.0
speed_premise = 3.0
time_hypothesis = 0.0

# the hypothesis refers to the time travelled, which can be calculated from the premise using the formula time = distance/speed
# compute the time travelled from the premise
time_premise = distance_premise / speed_premise

if time_hypothesis != time_premise:
    # check if the time in the hypothesis contradicts the time calculated from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
