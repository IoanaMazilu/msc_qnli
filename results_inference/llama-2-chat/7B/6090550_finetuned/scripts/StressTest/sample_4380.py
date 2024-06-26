total_time_premise = 1 + 3
total_time_hypothesis = 8
speed_premise = 50
speed_hypothesis = 50

# the hypothesis refers to the total time and speed of driving mentioned in the premise
if total_time_hypothesis!= total_time_premise:
    # check if the total time in the hypothesis contradicts the total time reported in the premise
    label = "contradiction"
elif speed_hypothesis!= speed_premise:
    # check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
