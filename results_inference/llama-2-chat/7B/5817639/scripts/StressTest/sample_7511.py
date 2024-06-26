hour_premise = 1 + 3 = 4
mph_premise = 50 + 60 = 110
mph_hypothesis = 70

# the hypothesis refers to the total time and speed mentioned in the premise
if hour_hypothesis <= hour_premise:
    # check if the estimate of 'hour_hypothesis' contradicts the total time in the premise
    label = "contradiction"
elif mph_hypothesis!= mph_premise:
    # check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
