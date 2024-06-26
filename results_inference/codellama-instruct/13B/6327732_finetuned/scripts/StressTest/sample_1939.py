time_john_premise = 60
time_todd_premise = 60
time_john_hypothesis = 30
time_todd_hypothesis = 60

# the hypothesis refers to the time it takes John and Todd to rake the lawn
if time_john_hypothesis!= time_john_premise:
    # check if the hypothesis value for John contradicts the premise value
    label = "contradiction"
elif time_todd_hypothesis!= time_todd_premise:
    # check if the hypothesis value for Todd contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
