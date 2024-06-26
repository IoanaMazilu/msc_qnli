time_john_premise = 30
time_todd_premise = 60
time_john_hypothesis = 60
time_todd_hypothesis = 60

# the hypothesis refers to the time it takes to rake a lawn for John and Todd
if time_john_hypothesis >= time_john_premise:
    # check if the estimate of 'time_john_hypothesis' contradicts the time it takes for John in the premise
    label = "contradiction"
elif time_todd_hypothesis!= time_todd_premise:
    # check if the time it takes for Todd in the hypothesis contradicts the time it takes for Todd in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
