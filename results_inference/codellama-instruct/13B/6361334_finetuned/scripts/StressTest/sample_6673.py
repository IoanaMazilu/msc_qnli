distance_premise = 5 * 40
distance_hypothesis = 1 * 40
time_premise = 3
time_hypothesis = 3

# the hypothesis refers to the time and speed mentioned in the premise
if time_hypothesis!= time_premise:
    # check if the number of hours in the hypothesis contradicts the number of hours mentioned in the premise
    label = "contradiction"
elif distance_hypothesis!= distance_premise:
    # check if the distance traveled in the hypothesis contradicts the distance traveled in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
