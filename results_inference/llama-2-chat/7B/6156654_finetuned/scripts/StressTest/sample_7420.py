floor_premise = 61
floor_hypothesis = 11
speed_premise = 57
speed_hypothesis = 57

# the hypothesis talks about the floor and speed of the elevator, which are also mentioned in the premise
if floor_hypothesis <= floor_premise:
    # check if the hypothesis value for the floor is less than or equal to the premise value
    label = "entailment"
elif speed_hypothesis!= speed_premise:
    # check if the hypothesis value for the speed is different from the premise value
    label = "contradiction"
else:
    # if the hypothesis values and estimates are the same as the premise ones, we can infer neutral
    label = "neutral"

print(label)
