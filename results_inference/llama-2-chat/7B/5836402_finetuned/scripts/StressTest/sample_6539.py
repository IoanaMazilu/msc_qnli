speed_premise = 30
speed_hypothesis = 60

# the hypothesis refers to the speed of driving mentioned in the premise
if speed_hypothesis!= speed_premise:
    # check if the speed in the hypothesis contradicts the speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
