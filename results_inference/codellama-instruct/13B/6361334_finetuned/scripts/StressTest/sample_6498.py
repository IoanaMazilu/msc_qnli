matthew_wake_premise = 1
matthew_wake_hypothesis = 1
distance_premise = 45
distance_hypothesis = 35

# the hypothesis refers to the distance traveled by Johnny and the time elapsed since Matthew woke up
if distance_hypothesis <= distance_premise:
    # check if the estimate of 'distance_hypothesis' contradicts the distance traveled in the premise
    label = "contradiction"
elif matthew_wake_hypothesis!= matthew_wake_premise:
    # check if the time elapsed in the hypothesis contradicts the time elapsed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
