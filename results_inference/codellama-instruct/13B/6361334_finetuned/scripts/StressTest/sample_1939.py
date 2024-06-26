time_john_premise = 60
time_todd_premise = 60
time_john_hypothesis = 30
time_todd_hypothesis = 60

# the hypothesis refers to the time it takes John and Todd to rake a lawn, which is also mentioned in the premise
if time_john_hypothesis!= time_john_premise:
    # check if the time it takes John in the hypothesis contradicts the time it takes John in the premise
    label = "contradiction"
elif time_todd_hypothesis!= time_todd_premise:
    # check if the time it takes Todd in the hypothesis contradicts the time it takes Todd in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)